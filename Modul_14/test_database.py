import sqlite3
dataB = sqlite3.connect('db.sqlite3')
cursor = dataB.cursor()
#cursor.execute("CREATE TABLE Students (id int, name Varchar(32), surname Varchar(32), age int, city Varchar(32))")
#cursor.execute("CREATE TABLE Courses (id int, name Varchar(32), time_start str, time_end str)")
#cursor.execute("CREATE TABLE Student_courses (student_id int, course_id int)")
cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'), (3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')])
cursor.executemany("INSERT INTO Courses (id, name, time_start, time_end) VALUES (?,?,?,?)", [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')])
cursor.executemany("INSERT INTO Student_courses (student_id, course_id) VALUES (?,?)", [(1, 1), (2, 1), (3, 1), (4, 2)])

cursor.execute("SELECT name, surname FROM Students WHERE age > 30")
print(f'Студенты старше 30 лет: \n{cursor.fetchall()}')
cursor.execute("SELECT name, surname FROM Students WHERE city = 'Spb'")
print(f'Студенты из Питера: \n{cursor.fetchall()}')

cursor.close()

import sqlite3
import unittest

class TestDatabaseOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Создание базы выполняется один раз для всех тестов"""
        cls.conn = sqlite3.connect(':memory:')
        cls.conn.execute("PRAGMA foreign_keys = ON") #Включение функциональности каскадного удаления
        cls.cursor = cls.conn.cursor()

        #Создаем таблицы
        cls.cursor.execute(
            "CREATE TABLE Students (id int PRIMARY KEY, name Varchar(32), surname Varchar(32), age int, city Varchar(32))")
        cls.cursor.execute("CREATE TABLE Courses (id int PRIMARY KEY, name Varchar(32), time_start str, time_end str)")
        cls.cursor.execute("""
            CREATE TABLE Student_courses (
                student_id int,
                course_id int,
                FOREIGN KEY(student_id) REFERENCES Students(id) ON DELETE CASCADE,
                FOREIGN KEY(course_id) REFERENCES Courses(id) ON DELETE CASCADE
            )
        """)

        #Добавляем тестовые данные
        cls.cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)",
                               [(1, 'Max', 'Brooks', 24, 'Spb'),
                                (2, 'John', 'Stones', 15, 'Spb'),
                                (3, 'Andy', 'Wings', 45, 'Manhester'),
                                (4, 'Kate', 'Brooks', 34, 'Spb')])
        cls.cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)",
                               [(1, 'python', '21.07.21', '21.08.21'),
                                (2, 'java', '13.07.21', '16.08.21')])
        cls.cursor.executemany("INSERT INTO Student_courses VALUES (?,?)",
                               [(1, 1), (2, 1), (3, 1), (4, 2)])
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        """Закрываем соединение с базой после всех тестов"""
        cls.conn.close()

    def test_add_student(self):
        """Тест добавления нового студента"""
        #Добавляем нового студента
        new_student = (5, 'Alex', 'Smith', 28, 'Moscow')
        self.cursor.execute("INSERT INTO Students VALUES (?,?,?,?,?)", new_student)
        self.conn.commit()

        #Проверяем, что студент добавлен
        self.cursor.execute("SELECT * FROM Students WHERE id = 5")
        result = self.cursor.fetchone()

        self.assertIsNotNone(result, "Студент не был добавлен в базу")
        self.assertEqual(result, new_student, "Данные студента не соответствуют ожидаемым")

    def test_add_course(self):
        """Тест добавления нового курса"""
        #Добавляем новый курс
        new_course = (3, 'sql', '01.09.21', '30.09.21')
        self.cursor.execute("INSERT INTO Courses VALUES (?,?,?,?)", new_course)
        self.conn.commit()

        #Проверяем, что курс добавлен
        self.cursor.execute("SELECT * FROM Courses WHERE id = 3")
        result = self.cursor.fetchone()

        self.assertIsNotNone(result, "Курс не был добавлен в базу")
        self.assertEqual(result, new_course, "Данные курса не соответствуют ожидаемым")

    def test_delete_student(self):
        """Тест удаления студента"""
        #Удаляем студента с id = 2
        student_id_to_delete = 2
        self.cursor.execute("DELETE FROM Students WHERE id = ?", (student_id_to_delete,))
        self.conn.commit()

        #Проверяем, что студент удален
        self.cursor.execute("SELECT * FROM Students WHERE id = ?", (student_id_to_delete,))
        result = self.cursor.fetchone()

        self.assertIsNone(result, "Студент не был удален из базы")

        #Проверяем, что записи о курсах студента удалены
        self.cursor.execute("SELECT * FROM Student_courses WHERE student_id = ?", (student_id_to_delete,))
        courses_result = self.cursor.fetchall()
        self.assertEqual(len(courses_result), 0, "Записи о курсах студента не были удалены")


if __name__ == '__main__':
    unittest.main()