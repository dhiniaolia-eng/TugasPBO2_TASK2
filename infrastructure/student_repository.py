from domain.entities import Mahasiswa

class StudentRepository:
    def __init__(self, db):
        self.db = db

    # Ubah dari get_all_students menjadi get_all
    def get_all(self):
        connection = self.db.get_connection()
        if not connection:
            return []
        
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT nim, nama, prodi, angkatan FROM students")
            rows = cursor.fetchall()
            return [Mahasiswa(row['nim'], row['nama'], row['prodi'], int(row['angkatan'])) for row in rows]
        except Exception as e:
            print(f"Error get_all: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

    def add(self, mhs: Mahasiswa):
        connection = self.db.get_connection()
        if not connection:
            return False
        
        cursor = connection.cursor()
        try:
            query = "INSERT INTO students (nim, nama, prodi, angkatan) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (mhs.nim, mhs.nama, mhs.prodi, mhs.angkatan))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error add: {e}")
            return False
        finally:
            cursor.close()
            connection.close()

    def update(self, mhs: Mahasiswa):
        connection = self.db.get_connection()
        if not connection:
            return False
        
        cursor = connection.cursor()
        try:
            query = "UPDATE students SET nama=%s, prodi=%s, angkatan=%s WHERE nim=%s"
            cursor.execute(query, (mhs.nama, mhs.prodi, mhs.angkatan, mhs.nim))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error update: {e}")
            return False
        finally:
            cursor.close()
            connection.close()

    def delete(self, nim: str):
        connection = self.db.get_connection()
        if not connection:
            return False
        
        cursor = connection.cursor()
        try:
            query = "DELETE FROM students WHERE nim=%s"
            cursor.execute(query, (nim,))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error delete: {e}")
            return False
        finally:
            cursor.close()
            connection.close()