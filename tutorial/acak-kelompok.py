import random

#list 15 mahasiswa untuk pembentukan 5 kelompok dengan masing-masing kelompok terdiri dari 3 mahasiswa
mahasiswa = ['adi', 'ani', 'putra', 'desi', 'dewi', 'dimas', 'putri', 'dani', 'ayu', 'reza', 'tika', 'andika', 'sari', 'ika', 'agus']

#random array mahasiswa
random.shuffle(mahasiswa)

#tampilkan 5 kelompok yang terdiri dari 3 mahasiswa per kelompok
for i in range(5):
    print("kelompok", i+1, "adalah", mahasiswa[i*3:(i*3)+3])
