import pymysql
def create_attendance_record(conn, student_id, course_id, attendance_date, status):
    print(student_id)
    print(course_id)
    print(attendance_date)
    print(status)

    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO attendance (student_id, course_id, attendance_date, status) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (student_id, course_id, attendance_date, status))
        conn.commit()
    except Exception as e:
        print("Error creating attendance record:", e)

def get_attendance_record(conn, attendance_id):
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM attendance WHERE id = %s"
            cursor.execute(sql, (attendance_id,))
            attendance_record = cursor.fetchone()
            return attendance_record
    except Exception as e:
        print("Error retrieving attendance record:", e)

def update_attendance_record(conn, attendance_id, student_id, course_id, attendance_date, status):
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE attendance SET student_id = %s, course_id = %s, attendance_date = %s, status = %s WHERE id = %s"
            cursor.execute(sql, (student_id, course_id, attendance_date, attendance_id, status))
    except Exception as e:
        print("Error updating attendance record:", e)

def delete_attendance_record(conn, attendance_id):
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM attendance WHERE id = %s"
            cursor.execute(sql, (attendance_id,))
    except Exception as e:
        print("Error deleting attendance record:", e)

def get_all_attendance_records(conn):
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM attendance"
            cursor.execute(sql)
            attendance_records = cursor.fetchall()
            return attendance_records
    except Exception as e:
        print("Error retrieving attendance records:", e)
