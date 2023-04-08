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


