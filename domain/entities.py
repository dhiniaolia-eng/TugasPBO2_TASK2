class Mahasiswa:
    def __init__(self, nim: str, nama: str, prodi: str, angkatan: int):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.angkatan = angkatan
    def to_dict(self):
        return {
            "nim": self.nim,
            "nama": self.nama,
            "prodi": self.prodi,
            "angkatan": self.angkatan
        }