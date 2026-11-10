from domain.entities import Mahasiswa
from infrastructure.student_repository import StudentRepository

class StudentUseCase:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def list_students(self):
        return self.repository.get_all()

    def create_student(self, nim: str, nama: str, prodi: str, angkatan: int):
        if not nim or not nama or not prodi or not angkatan:
            raise ValueError("Semua field wajib diisi!")        
        mhs = Mahasiswa(nim=nim, nama=nama, prodi=prodi, angkatan=int(angkatan))
        return self.repository.add(mhs)

    def update_student(self, nim: str, nama: str, prodi: str, angkatan: int):
        if not nim or not nama or not prodi or not angkatan:
            raise ValueError("Semua field wajib diisi!")
        mhs = Mahasiswa(nim=nim, nama=nama, prodi=prodi, angkatan=int(angkatan))
        return self.repository.update(mhs)

    def delete_student(self, nim: str):
        if not nim:
            raise ValueError("NIM tidak boleh kosong!")
        return self.repository.delete(nim)