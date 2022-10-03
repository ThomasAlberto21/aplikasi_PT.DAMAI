import streamlit as st
import pandas as pd


st.write(""" # Aplikasi Untuk Memberikan Tunjangan Kepada Karyawan PT.Damai """)
st.caption('Gaji Tetap 300.000 Perbulan')

nama_karyawan = st.text_input("Masukkan Nama Karyawan : ")
golongan = st.number_input("Masukkan Golongan Anda (1 / 2 / 3) : ", 0)
pendidikan = st.text_input("Masukkan Pendidikan Anda (SMA / D1 / D3 / S1) : ")
jam_kerja = st.number_input("Masukkan Jam Kerja : ", 0)
perjam_lembur = 3500
gaji = 3000000


# ! Logika golongan
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


# ! logika tunjangan pendidikan
if pendidikan == "SMA" or pendidikan == "sma":
    persentase = "2,5%"
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
    print("Jabatan Yang Anda Masukkan Tidak Ada")


# ! logika Jam kerja
if jam_kerja > 8:
    jumlah_jam = (jam_kerja - 8) * perjam_lembur
else:
    jumlah_jam = 0


total_tunjangan = tunjangan_golongan + tunjangan_pendidikan
total_gaji = gaji + total_tunjangan + perjam_lembur


# st.success(f"Karyawan Yang Bernama        :  {nama_karyawan}")
# st.success(f"Honor Yang Diterima")
# st.success(f"Tunjangan Jabatan          Rp.  {tunjangan_golongan}")
# st.success(f"Tunjangan Pendidikan       Rp.  {tunjangan_pendidikan}")
# st.success(f"Honor Lembur               :  {jumlah_jam}")
# st.success(f"Total Tunjangan Semuanya Adalah Rp.  {total_gaji}")


# col1, col2 = st.columns(2)

# with col1:
#     st.success(f"Karyawan Yang Bernama        :  {nama_karyawan}")


# with col2:
#     st.success(f"Honor Yang Diterima: ")
#     st.success(f"Tunjangan Jabatan               Rp.  {tunjangan_golongan}")
#     st.success(f"Tunjangan Pendidikan            Rp.  {tunjangan_pendidikan}")
#     st.success(f"Honor Lembur                    Rp.  {jumlah_jam}")
#     st.success(f"Total Tunjangan Semuanya Adalah Rp.  {total_gaji}")


with st.sidebar:
    st.success(f"Karyawan Yang Bernama        :  {nama_karyawan}")
    st.success(f"Honor Yang Diterima: ")
    st.success(
        f"Tunjangan Jabatan               Rp.  {tunjangan_golongan}")
    st.success(
        f"Tunjangan Pendidikan            Rp.  {tunjangan_pendidikan}")
    st.success(f"Honor Lembur                    Rp.  {jumlah_jam}")
    st.success(f"Total Tunjangan Semuanya Adalah Rp.  {total_gaji}")
