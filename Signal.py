import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

class Start:
    def  __init__(self,time,alpha=60,r=500,fd=80000,fs=20000,period=5,A=1):
        self.A=A
        self.fd=fd
        self.fs=fs
        self.period=period
        self.time=time
        self.r=r+500 * np.random.randint(0,5)
        self.alpha=alpha*np.random.rand(1)-30
        self.t=np.arange(0,self.period,1/self.fd) #массив временных отсчетов

    def send(self):

      num = int(np.round(self.time*self.fd))
      signal=np.zeros(self.t.size)
      signal[0:num]=self.A*np.sin(2*np.pi*self.fs*self.t[0:num])
      lenk=len(self.t)

      return(signal,self.t,self.fd,self.fs,self.A,num,lenk,self.r)

class Echo:
    def __init__(self,fs,signal,num,A,t,fd,r,d=0.3,c=1500):
        self.fs=fs
        self.signal=signal
        self.num=num
        self.A=A
        self.t=t
        self.fd=fd
        self.r=r
        self.d=d
        self.c=c

    def submarine(self):

        bliks=np.random.randint(3,6)
        signal1=self.signal
        signal2=self.signal
        testx=[]
        testy=[]
        testx.append(0)
        testy.append(0)
        alpha = np.random.randint(45, 135)
        phi = np.random.randint(180)
        alpha = np.deg2rad(alpha)
        phi = np.deg2rad(phi)
        for i in range(bliks):
            x = self.r*np.cos(alpha) + 20*i*np.cos(phi)
            y = self.r*np.sin(alpha) + 20*i*np.sin(phi)
            testx.append(x)
            testy.append(y)
            r_blik=np.sqrt(x**2+y**2)
            phi_blic = np.arctan(x/y)
            dphi = 2*np.pi*self.fs*self.d/self.c*np.sin(phi_blic)
            tay = 2 * r_blik / self.c
            num_tau = int(np.round(tay * self.fd))
            t_echo = t[num_tau:num_tau + self.num]
            signal1[num_tau:num_tau + self.num] = signal1[num_tau:num_tau + self.num] + self.A * np.sin(2 * np.pi * self.fs * t_echo / fd)
            signal2[num_tau:num_tau + self.num] = signal2[num_tau:num_tau + self.num] + self.A * np.sin(2 * np.pi * self.fs * t_echo/fd + dphi)
        plt.scatter(testx, testy)
        plt.show()

        return (signal1, signal2, testx,testy)

    def fake(self):

        signal1 = self.signal
        signal2 = self.signal
        testx = []
        testy = []
        testx.append(0)
        testy.append(0)
        alpha = np.random.randint(45, 135)
        alpha = np.deg2rad(alpha)
        phi = alpha
        for i in range(3):
            x = self.r * np.cos(alpha) + 10 * i * np.cos(phi)
            y = self.r * np.sin(alpha) + 10 * i * np.sin(phi)
            testx.append(x)
            testy.append(y)
            r_blik = np.sqrt(x * x + y * y)
            phi_blic = np.arctan(x / y)
            dphi = 2 * np.pi * self.fs * self.d / self.c * np.sin(phi_blic)
            tay = 2 * r_blik / self.c
            num_tau = int(np.round(tay * self.fd))
            t_echo = t[num_tau:num_tau + self.num]
            signal1[num_tau:num_tau + self.num] = signal1[num_tau:num_tau + self.num] + self.A * np.sin(2 * np.pi * self.fs * t_echo/fd)
            signal2[num_tau:num_tau + self.num] = signal2[num_tau:num_tau + self.num] + self.A * np.sin(2 * np.pi * self.fs * t_echo/fd + dphi)
        plt.scatter(testx, testy)
        plt.show()

        return (signal1, signal2, testx,testy)

    def cloud(self):

        signal1 = self.signal
        signal2 = self.signal
        testx = []
        testy = []
        testx.append(0)
        testy.append(0)
        alpha = np.random.randint(45, 135)
        alpha = np.deg2rad(alpha)
        for i in range(20):
            x = self.r * np.cos(alpha) + 120*np.random.rand(1)
            y = self.r * np.sin(alpha) + 120*np.random.rand(1)
            testx.append(x)
            testy.append(y)
            r_blik = np.sqrt(x * x + y * y)
            phi_blic = np.arctan(x / y)
            dphi = 2 * np.pi * self.fs * self.d / self.c * np.sin(phi_blic)
            tay = 2 * r_blik / self.c
            num_tau = np.round(tay * self.fd)
            t_echo = t[num_tau:num_tau + self.num]
            signal1[num_tau:num_tau + self.num] = signal1[num_tau:num_tau + self.num] + self.A * np.sin(2 * np.pi * self.fs * t_echo/fd)
            signal2[num_tau:num_tau + self.num] = signal2[num_tau:num_tau + self.num] + self.A * np.sin(2 * np.pi * self.fs * t_echo/fd + dphi)
        plt.scatter(testx, testy)
        plt.show()

        return (signal1, signal2, testx,testy)

#class Water:


start=Start(time=0.2)
(signal,t,fd,fs,A,num,lenk,r)=start.send()
echo = Echo(signal,t,fd,fs,A,num,r)
(signal1,signal2,testx,testy)=echo.submarine()
#plt.plot(t,signal)
#plt.show()