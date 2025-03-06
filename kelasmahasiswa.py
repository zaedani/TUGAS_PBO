class Mahasiswa :
    def __init__(self, nama, nim, prodi, angkatan):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.angkatan = angkatan

    def praktikum(self):
        return f"{self.nama}aktif dalam kegiatan oraganisasi"
    
    def beroganisasi(self):
        return f"{self.nama}aktif dalam kegiatan organisasi"
    
    def mengerjakan_tugas(self):
        return f"{self.nama}atif dalam mengerjakan tugas"
    
mahasiswa1 = Mahasiswa("nasril", 24311380, "management", 24)
mahasiswa2 = Mahasiswa("zidan", 710240031, "teknik informatika", 24)

print(f"nama mahasiswa: {mahasiswa1.nama}")
print(f"nim mahasiswa: {mahasiswa1.nim}")
print(f"prodi mahasiswa: {mahasiswa1.prodi}")
print(f"angkatan mahasiswa: {mahasiswa1.angkatan}")

print(f"nama mahasiswa: {mahasiswa2.nama}")
print(f"nim mahasiswa: {mahasiswa2.nim}")
print(f"prodi mahasiswa: {mahasiswa2.prodi}")
print(f"angkatan mahasiswa: {mahasiswa2.angkatan}")