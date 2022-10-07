import streamlit as st
import pandas as pd

st.write(""" # Aplikasi Untuk Memberikan TUnjangan Kepada Karyawan PT.DAMAI""")
st.caption("Gaji Tetap Rp.300.000 Perbulan")


# ? masukkan inputan
nama_karyawan = st.text_input("Masukkan Nama Karyawan")
golongan = st.number_input("Masukkan Golongan(1 / 2 / 3)", 0)
pendidikan = st.text_input("Masukkan Pendidikan Anda (SMA / D1 / D3 / S1)")
jam_kerja = st.number_input("Masukkan Jam Kerja", 0)
perjam_lembur = 3500
gaji = 300000


# ! Logika Golongan
if golongan == 1:
    persentase = "5%"
    tunjangan_golongan = 5 * gaji / 100
elif golongan == 2:
    persentase = "10%"
    tunjangan_golongan = 10 * gaji / 100
elif golongan == 3:
    persentase = "15%"
    tunjangan_golongan = 15 * gaji / 100
else:
    print("Golongan Yang Anda Masukkan Tidak Ada")


# !  logika pendidikan
if pendidikan == "SMA" or pendidikan == "sma":
    persentase = "2.5%"
    tunjangan_pendidikan = 2.5 * gaji / 100
elif pendidikan == "D1" or pendidikan == "d1":
    persentase = "5%"
    tunjangan_pendidikan = 5 * gaji / 100
elif pendidikan == "D3" or pendidikan == "d3":
    persentase = "20%"
    tunjangan_pendidikan = 20 * gaji / 100
elif pendidikan == "S1" or pendidikan == "s1":
    persentase = "30%"
    tunjangan_pendidikan = 30 * gaji / 100
else:
    print("Pendidikan Yang Anda Masukkan Tidak Ada")


# ! logika jam kerja
if jam_kerja > 8:
    jumlah_jam = (jam_kerja - 8) * perjam_lembur
else:
    jumlah_jam = 0

total_tunjangan = tunjangan_pendidikan + tunjangan_golongan
total_gaji = gaji + total_tunjangan + jumlah_jam

with st.sidebar:
    st.success(f"Karyawan Yang Bernama : {nama_karyawan} ")
    st.success(f"Honor yang Diterima :")
    st.success(f"Tunjangan Golongan                 Rp. {tunjangan_golongan}")
    st.success(
        f"Tunjangann Pendidikan              Rp. {tunjangan_pendidikan}")
    st.success(f"Honor Lembur Sebesar               Rp. {jumlah_jam}")
    st.success(f"Total Tunjangan Semuannya Adalah   Rp. {total_gaji}")
