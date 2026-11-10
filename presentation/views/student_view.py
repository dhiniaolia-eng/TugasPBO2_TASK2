import tkinter as tk
from tkinter import ttk, messagebox

class StudentView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Manajemen Mahasiswa")
        self.geometry("700x500")

        self.controller = None

        # Title
        tk.Label(self, text="Sistem Informasi Data Mahasiswa", font=("Arial", 16, "bold")).pack(pady=10)

        # Form Input Frame
        form_frame = tk.Frame(self)
        form_frame.pack(pady=5, padx=10, fill=tk.X)

        tk.Label(form_frame, text="NIM:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.entry_nim = tk.Entry(form_frame)
        self.entry_nim.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(form_frame, text="Nama:").grid(row=0, column=2, sticky="w", padx=5, pady=2)
        self.entry_nama = tk.Entry(form_frame)
        self.entry_nama.grid(row=0, column=3, padx=5, pady=2)

        tk.Label(form_frame, text="Prodi:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.entry_prodi = tk.Entry(form_frame)
        self.entry_prodi.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(form_frame, text="Angkatan:").grid(row=1, column=2, sticky="w", padx=5, pady=2)
        self.entry_angkatan = tk.Entry(form_frame)
        self.entry_angkatan.grid(row=1, column=3, padx=5, pady=2)

        # Button Frame
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Tambah", bg="#4CAF50", fg="white", width=10, command=self._on_add).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Update", bg="#2196F3", fg="white", width=10, command=self._on_update).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Hapus", bg="#f44336", fg="white", width=10, command=self._on_delete).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Reset Form", bg="#9E9E9E", fg="white", width=10, command=self.clear_form).pack(side=tk.LEFT, padx=5)

        # Table Treeview
        self.tree = ttk.Treeview(self, columns=("NIM", "Nama", "Prodi", "Angkatan"), show="headings")
        self.tree.heading("NIM", text="NIM")
        self.tree.heading("Nama", text="Nama Mahasiswa")
        self.tree.heading("Prodi", text="Program Studi")
        self.tree.heading("Angkatan", text="Angkatan")

        self.tree.column("NIM", width=120)
        self.tree.column("Nama", width=200)
        self.tree.column("Prodi", width=150)
        self.tree.column("Angkatan", width=100)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self._on_select_row)

    def set_controller(self, controller):
        self.controller = controller

    def display_students(self, students):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for mhs in students:
            self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.prodi, mhs.angkatan))

    def clear_form(self):
        self.entry_nim.config(state="normal")
        self.entry_nim.delete(0, tk.END)
        self.entry_nama.delete(0, tk.END)
        self.entry_prodi.delete(0, tk.END)
        self.entry_angkatan.delete(0, tk.END)

    def _on_select_row(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")
            self.entry_nim.delete(0, tk.END)
            self.entry_nim.insert(0, values[0])
            self.entry_nim.config(state="disabled") # Lock NIM saat edit
            self.entry_nama.delete(0, tk.END)
            self.entry_nama.insert(0, values[1])
            self.entry_prodi.delete(0, tk.END)
            self.entry_prodi.insert(0, values[2])
            self.entry_angkatan.delete(0, tk.END)
            self.entry_angkatan.insert(0, values[3])

    def _on_add(self):
        if self.controller:
            self.controller.add_student(
                self.entry_nim.get(),
                self.entry_nama.get(),
                self.entry_prodi.get(),
                self.entry_angkatan.get()
            )

    def _on_update(self):
        if self.controller:
            self.entry_nim.config(state="normal")
            nim = self.entry_nim.get()
            self.entry_nim.config(state="disabled")
            self.controller.update_student(
                nim,
                self.entry_nama.get(),
                self.entry_prodi.get(),
                self.entry_angkatan.get()
            )

    def _on_delete(self):
        if self.controller:
            self.entry_nim.config(state="normal")
            nim = self.entry_nim.get()
            self.entry_nim.config(state="disabled")
            if messagebox.askyesno("Konfirmasi", f"Yakin ingin menghapus NIM {nim}?"):
                self.controller.delete_student(nim)