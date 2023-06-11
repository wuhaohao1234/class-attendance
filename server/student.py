import pymysql

def get_all_students(conn):
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM students"
            cursor.execute(sql)
            rows = cursor.fetchall()
            students = []
            for row in rows:
                student = {
                    'id': row['id'],
                    'name': row['name'],
                    'email': row['email']
                }
                students.append(student)
            return students
    except Exception as e:
        return {'error': str(e)}

def get_student(conn, student_id):
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM students WHERE id = %s"
            cursor.execute(sql, (student_id,))
            row = cursor.fetchone()
            if row:
                student = {
                    'id': row['id'],
                    'name': row['name'],
                    'email': row['email']
                }
                return student
            else:
                return {'message': 'Student not found'}
    except Exception as e:
        return {'error': str(e)}

def add_student(conn, name, email):
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO students (name, email) VALUES (%s, %s)"
            cursor.execute(sql, (name, email))
            conn.commit()
            return {'message': 'Student added successfully'}
    except Exception as e:
        return {'error': str(e)}

def update_student(conn, student_id, name, email):
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE students SET name = %s, email = %s WHERE id = %s"
            cursor.execute(sql, (name, email, student_id))
            conn.commit()
            return {'message': 'Student updated successfully'}
    except Exception as e:
        return {'error': str(e)}

def delete_student(conn, student_id):
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM students WHERE id = %s"
            cursor.execute(sql, (student_id,))
            conn.commit()
            return {'message': 'Student deleted successfully'}
    except Exception as e:
        return {'error': str(e)}
