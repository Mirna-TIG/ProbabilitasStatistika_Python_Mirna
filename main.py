import pandas as pd
import matplotlib.pyplot as plt

# 1. Baca & rapikan data Excel
path = "mirna.xlsx"
dataraw = pd.read_excel(path, header=None)
dataraw = dataraw.iloc[1:].reset_index(drop=True)
dataraw.columns = ['NIM', 'Nama', 'Kuis', 'UTS', 'UAS', 'Nilai Akhir', 'Grade']

# 2. Hitung frekuensi Grade & URUTKAN KATEGORI secara manual (F ke A)
datafrq = pd.crosstab(index=dataraw["Grade"], columns="Frekuensi")

# Mengurutkan urutan Grade sesuai gambar: F, C, BC, B, AB, A
urutan_grade = ['F', 'C', 'BC', 'B', 'AB', 'A']
datafrq = datafrq.reindex(urutan_grade).fillna(0)

# Menentukan urutan warna spesifik sesuai contoh gambar:
# F=Merah, C=Oranye, BC=Kuning-Hijau, B=Biru, AB=Hijau, A=Cyan/Turquoise
color_map = {
    'F': '#d62728',    # Merah
    'C': '#ff7f0e',    # Oranye
    'BC': '#bcbd22',   # Kuning-Hijau
    'B': '#1f77b4',    # Biru
    'AB': '#2ca02c',   # Hijau
    'A': '#17becf'     # Cyan
}
warna_list = [color_map[g] for g in datafrq.index]


# --- GRAFIK 1: Grafik Garis ---
plt.figure(1)
plt.plot(datafrq.index, datafrq['Frekuensi'], marker='o', linewidth=2, color='#1f77b4', markerfacecolor='#ff7f0e', markeredgecolor='black')
plt.title("Grafik Garis - Frekuensi Nilai per Grade\n(Mirna)", fontweight='bold')
plt.xlabel("Grade")
plt.ylabel("Frekuensi (jumlah mahasiswa)")
plt.grid(True, linestyle='-', alpha=0.5)

# Angka di atas titik
for i, txt in enumerate(datafrq['Frekuensi']):
    plt.annotate(int(txt), (datafrq.index[i], txt), textcoords="offset points", xytext=(0, 5), ha='center')


# --- GRAFIK 2: Grafik Batang ---
plt.figure(2)
bars = plt.bar(datafrq.index, datafrq['Frekuensi'], color=warna_list, edgecolor='black')
plt.title("Grafik Batang - Frekuensi Nilai per Grade\n(Mirna)", fontweight='bold')
plt.xlabel("Grade")
plt.ylabel("Frekuensi (jumlah mahasiswa)")
plt.grid(True, linestyle='-', alpha=0.5, axis='y')

# Angka di atas batang
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval), ha='center', va='bottom')


# --- GRAFIK 3: Pie Chart ---
plt.figure(3)
explode = [0.05] * len(datafrq)
plt.pie(datafrq['Frekuensi'], labels=datafrq.index, autopct='%1.0f%%', 
        startangle=90, explode=explode, colors=warna_list)
plt.title("Pie Chart - Persentase Grade\n(Mirna)", fontweight='bold')

# Tampilkan grafik
plt.show()

# --- Statistika Deskriptif ---
# Konversi data ke numerik agar terhindar dari eror tipe data
dataraw["Nilai Akhir"] = pd.to_numeric(dataraw["Nilai Akhir"], errors='coerce')
dt = dataraw["Nilai Akhir"]

# Hitung statistika dasar dengan describe()
stats = dt.describe()

# Tambahkan nilai statistik deskriptif lainnya
stats['Standard Error'] = dt.sem()
stats['Median'] = dt.median()
stats['Mode'] = dt.mode().iloc[0]
stats['variance'] = dt.var()
stats['range'] = dt.max() - dt.min()
stats['skewness'] = dt.skew()
stats['kurtosis'] = dt.kurtosis()

# Tampilkan hasil di terminal
print(stats)