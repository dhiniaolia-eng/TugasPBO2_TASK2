from tkinter import messagebox

class StudentController:
    def __init__(self, usecase, view):
        self.usecase = usecase
        self.view = view
        self.view.set_controller(self)

    def load_students(self):
        students = self.usecase.list_students()
        self.view.display_students(students)

    def add_student(self, nim, nama, prodi, angkatan):
        try:
            success = self.usecase.create_student(nim, nama, prodi, angkatan)
            if success:
                messagebox.showinfo("Sukses", "Data mahasiswa berhasil ditambahkan!")
                self.view.clear_form()
                self.load_students()
            else:
                messagebox.showerror("Gagal", "Gagal menyimpan data ke database.")
        except Exception as e:
            messagebox.showwarning("Peringatan", str(e))

    def update_student(self, nim, nama, prodi, angkatan):
        try:
            success = self.usecase.update_student(nim, nama, prodi, angkatan)
            if success:
                messagebox.showinfo("Sukses", "Data mahasiswa berhasil diperbarui!")
                self.view.clear_form()
                self.load_students()
            else:
                messagebox.showerror("Gagal", "Gagal memperbarui data di database.")
        except Exception as e:
            messagebox.showwarning("Peringatan", str(e))

    def delete_student(self, nim):
        try:
            success = self.usecase.delete_student(nim)
            if success:
                messagebox.showinfo("Sukses", "Data mahasiswa berhasil dihapus!")
                self.view.clear_form()
                self.load_students()
            else:
                messagebox.showerror("Gagal", "Gagal menghapus data dari database.")
        except Exception as e:
            messagebox.showwarning("Peringatan", str(e))