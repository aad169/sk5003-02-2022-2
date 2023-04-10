#1. Buatlah suatu modul yang berisikan suatu fungsi untuk menghitung volume dan luas permukaan kubus
#  dan balok. Tampilkan screenshot dari code program yang Anda bikin beserta output nya.

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
