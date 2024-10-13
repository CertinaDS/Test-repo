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