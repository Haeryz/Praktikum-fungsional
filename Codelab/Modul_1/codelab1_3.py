
#TO_DO 1
# HANYA CONTOH, silahkan dimodif
nilai_mahasiswa = {
    "Rifai": {"P.WEB": 90, "P.FUNGSIONAL": 85, "P.MOBILE": 85},
    "Fathul": {"P.WEB": 90, "P.FUNGSIONAL": 85, "P.MOBILE": 85},
    "Iqbal": {"P.WEB": 90, "P.FUNGSIONAL": 85, "P.MOBILE": 85},
    "Adi": {"P.WEB": 90, "P.FUNGSIONAL": 85, "P.MOBILE": 85},
    "Asep": {"P.WEB": 90, "P.FUNGSIONAL": 85, "P.MOBILE": 85}
}

#TO_DO 2
# Function each average
def rata_rata_mahasiswa(nilai_mahasiswa):
    rata_rata_mahasiswa = {}
    for mahasiswa, nilai in nilai_mahasiswa.items():
        rata_rata = sum(nilai.values())
        rata_rata = rata_rata / len(nilai)
        rata_rata_mahasiswa[mahasiswa] = rata_rata
    return rata_rata_mahasiswa


#TO_DO 3
# Function all average
def rata_rata_semua_mahasiswa(nilai_mahasiswa):
    total_nilai = 0
    total_matakuliah = 0
    for nilai in nilai_mahasiswa.values():
        total_nilai += sum(nilai.values())
        total_matakuliah += len(nilai)
    return total_nilai / total_matakuliah

rata_rata_mahasiswa = rata_rata_mahasiswa(nilai_mahasiswa)
for mahasiswa, rata_rata in rata_rata_mahasiswa.items():
    print(f"Nilai rata-rata {mahasiswa} adalah {rata_rata:.2f}")
    
rata_rata_semua_mahasiswa = rata_rata_semua_mahasiswa(nilai_mahasiswa)
print(f"Nilai rata-rata semua mahasiswa adalah {rata_rata_semua_mahasiswa:.2f}")