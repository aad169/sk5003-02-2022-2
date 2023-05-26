## Tugas Tutorial 5 / Ahmad Mushawir / 20922307
### Program ini berfungsi untuk melakukan evaluasi performa sekolah pada data. Data yang digunakan didapat dari kaggle.com yaitu data Student Performance Dataset. Dimana data ini menampilkan data 395 siswa serta nilai yang mereka miliki dalam 3 periode. Program ini akan menampilkan performa antar 2 sekolah yang ada di dataset ini.

Tugas 5 Tutorial.py
```py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#baca data dari csv
raw = pd.read_csv('student_data.csv')

#liat summary data
raw.describe()

#cek ada data kosong
raw.isnull().sum()

#tambahkan kolom nilai rata2 masing2 student
raw['averageG'] = (raw.G1+raw.G2+raw.G3)/3

#melihat sebaran data
def School(row):
    if row=='GP':
        return 'blue'
    elif row=='MS':
        return 'red'
#set warna permasing masing sekolah
color = raw['school'].apply(School)

#tampulkan sebaran data
plt.scatter(raw.index, raw.averageG, c=color)
plt.xlabel('Siswa ke-')
plt.ylabel('Rata-rata')
plt.show()


#hanya mengambil data yang mau dianalisa
data = raw[['school', 'averageG']].copy()

#gabungkan berdasarkan sekolah
data.groupby('school').mean()

#tampilkan hasil
x = plt.subplots(figsize =(6,6))
x = sns.barplot(data=data, x="school", y="averageG", palette='summer')
x.set_xlabel ("Sekolah",fontsize=12)
x.set_ylabel ("Rata-rata",fontsize=12)
x.set_title  ("Rata-rata nilai siswa berdasarkan sekolah",fontsize =15)
sns.set_style("whitegrid")
plt.show()
```
Ini hasil sebaran data nilai rata-rata seluruh siswa. Titik biru menunjukkan sekolah GP, titik merah menunjukkan sekolah MS

![image](https://github.com/aad169/sk5003-02-2022-2/assets/127568994/323a63fe-fb59-4fa4-912a-2a642702648b)

Berikut adalah hasil nilai rata-rata siswa berdasarkan sekolah

![image](https://github.com/aad169/sk5003-02-2022-2/assets/127568994/38bffc80-1347-4a61-aa70-d944d03c4ecb)


