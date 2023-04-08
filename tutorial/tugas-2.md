# Tugas 2 Tutorial
### 1. Buatlah suatu modul yang berisikan suatu fungsi untuk menghitung volume dan luas permukaan kubus dan balok. Tampilkan screenshot dari code program yang Anda bikin beserta output nya.

Code:
```py
#function untuk menghitung luas kubus dengan parameter x
def luasKubus(x):
    return 6*(x*x)
#function untuk menghitung volume kubus dengan parameter x
def volumeKubus(x):
    return x*x*x
#function untuk menghitung luas balok dengan parameter x, y dan z
def luasBalok(x, y, z):
    return 2*((x*y)+(y*z)+(x*z))
#function untuk menghitung volume balok dengan parameter x, y dan z
def volumeBalok(x, y, z):
    return x*y*z
#meminta input user untuk menetukan luas dan volume kubus
x = int(input("Masukkan panjang sisi kubus = "))
#menampilkan output luas dan volume kubus sesuai dengan input parameter dari user
print("luas kubus dengan panjang sisi",x,"adalah",luasKubus(x))
print("volume kubus dengan panjang sisi",x,"adalah",volumeKubus(x))
#meminta input user untuk menetukan luas dan volume balok
a = int(input("Masukkan panjang sisi balok = "))
b = int(input("Masukkan lebar sisi balok = "))
c = int(input("Masukkan tinggi sisi balok = "))
#menampilkan output luas dan volume balok sesuai dengan input parameter dari user
print("luas balok dengan panjang sisi",a,", lebar sisi",b,"dan tinggi sisi",c,"adalah",luasBalok(a,b,c))
print("volume balok dengan panjang sisi",a,", lebar sisi",b,"dan tinggi sisi",c,"adalah",volumeBalok(a,b,c))
```
Output:
```console
Masukkan panjang sisi kubus = 4
luas kubus dengan panjang sisi 4 adalah 96
volume kubus dengan panjang sisi 4 adalah 64
Masukkan panjang sisi balok = 2
Masukkan lebar sisi balok = 3
Masukkan tinggi sisi balok = 4
luas balok dengan panjang sisi 2 , lebar sisi 3 dan tinggi sisi 4 adalah 52
volume balok dengan panjang sisi 2 , lebar sisi 3 dan tinggi sisi 4 adalah 24
```

### 2. Tentukan output dari program tersebut dan berikan penjelasan singkat mengenai modul yang digunakan.
```py
from math import sinh, exp, e, pi
x = 2*pi
r1 = sinh(x)
r2 = 0.5*(exp(x) - exp(-x))
r3 = 0.5*(e**x - e**(-x))
print("Nilai r1=\n", r1)
print("Nilai r2=\n", r2)
print("Nilai r2=\n", r3) 
```
Output dari code tersebut adalah
```console
Nilai r1=
 267.74489404101644
Nilai r2=
 267.74489404101644
Nilai r2=
 267.7448940410163
```
Modul math adalah modul built-in dari python yang dapat digunakan untuk perhitungan-perhitungan matematika. 
Pada code ini hanya mengambil beberapa function dan attribute di dalam modul math yaitu sinh, exp, e, dan pi
- function sinh(x) berfungsi untuk memberikan nilai hiperbolik sinus dari suatu angka x
- function exp(x) berfungsi untuk memberikan hasil nilai pangkat suatu angka x dari bilangan euler (E)
- atribut e berfungsi untuk memberikan nilai dari bilangan euler (E) 
- atribut pi berfungsi untuk memberikan nilai dari bilangan pi

### 3. Tentukan output dari program tersebut dan jelaskan dengan singkat mengenai modul tersebut. Kemudian, buatlah juga suatu program yang menggunakan modul random.
```py
import random 

print('Random number from 0 to 1 :', random.random()) 
print('Uniform Distribution between [1,10] :', random.uniform(1, 10)) 
print('Gaussian Distribution with mean = 0.5 and standard deviation = 1.5 :', random.gauss(0.5, 1.5)) 
print('Exponential Distribution with lambda = 0.95 :', random.expovariate(0.95)) 
print('Normal Distribution with mean = 1 and standard deviation = 3.8:', random.normalvariate(1, 3.8))
```
output dari code tersebut adalah
```console
Random number from 0 to 1 : 0.7632939515958689
Uniform Distribution between [1,10] : 5.974400397042564
Gaussian Distribution with mean = 0.5 and standard deviation = 1.5 : -1.2831672015880553
Exponential Distribution with lambda = 0.95 : 2.2513731859353276
Normal Distribution with mean = 1 and standard deviation = 3.8: 6.97954521878103
```
Modul random adalah modul built-in dari python yang dapat digunakan untuk memberikan nilai random.
Ada banyak metode untuk pengambilan nilai random pada modul ini. Contohnya adalah:
- uniform(x, y) berfungsi untuk mengambil nilai random dengan tipe float antara x dan y
- gauss(x, y) berfungsi untuk mengambil nilai random berdasarkan distribusi gauss dengan parameter mean(x) dan standar deviasi(y)
- expovariate(x) berfungsi untuk mengambil nilai random berdasarkan distribusi eksponensial dengan parameter x adalah lambda
- normalvariate(x, y) berfungsi untuk mengambil nilai random berdasarkan distribusi normal dengan parameter mean(x) dan standar deviasi(y)

Berikut adalah program pengembangan yang dibuat dengan modul random.<br>
Program ini berfungsi untuk membuat kelompok secara acak pada sejumlah mahasiswa
```py
import random

#list 15 mahasiswa untuk pembentukan 5 kelompok dengan masing-masing kelompok terdiri dari 3 mahasiswa
mahasiswa = ['adi', 'ani', 'putra', 'desi', 'dewi', 'dimas', 'putri', 'dani', 'ayu', 'reza', 'tika', 'andika', 'sari', 'ika', 'agus']

#random array mahasiswa
random.shuffle(mahasiswa)

#tampilkan 5 kelompok yang terdiri dari 3 mahasiswa per kelompok
for i in range(5):
    print("kelompok", i+1, "adalah", mahasiswa[i*3:(i*3)+3])
```
output dari program tersebut adalah
```console
kelompok 1 adalah ['ayu', 'dani', 'agus']
kelompok 2 adalah ['tika', 'putri', 'ika']
kelompok 3 adalah ['reza', 'dimas', 'adi']
kelompok 4 adalah ['ani', 'desi', 'andika']
kelompok 5 adalah ['dewi', 'sari', 'putra']
```
