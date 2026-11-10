from infrastructure.database import Database
from infrastructure.student_repository import StudentRepository
from usecases.student_usecase import StudentUseCase
from presentation.views.student_view import StudentView
from presentation.controllers.student_controller import StudentController

def main():
    # 1. Inisialisasi Database & Repository
    db = Database(host="localhost", user="root", password="", database="db_kampus")
    repo = StudentRepository(db)

    # 2. Inisialisasi Use Case
    usecase = StudentUseCase(repo)

    # 3. Inisialisasi View & Controller
    view = StudentView()
    controller = StudentController(usecase, view)

    # 4. Muat Data & Jalankan Aplikasi GUI
    controller.load_students()
    view.mainloop()

if __name__ == "__main__":
    main()