import pymysql
# 获取所有老师
def get_all_teachers(conn):
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM teachers"
            cursor.execute(sql)
            teachers = cursor.fetchall()
            return teachers
    finally:
        print('ok')

# 添加老师
def add_teacher(conn, teacher_data):
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO teachers (name, email) VALUES (%s, %s)"
            cursor.execute(sql, (teacher_data['name'], teacher_data['email']))
            conn.commit()
    finally:
        print('ok')

# 删除老师
def delete_teacher(conn, teacher_id):
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM teachers WHERE id = %s"
            cursor.execute(sql, (teacher_id,))
            conn.commit()
    finally:
        print('ok')

# 更新老师
def update_teacher(conn, teacher_id, teacher_data):
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE teachers SET name = %s, email = %s WHERE id = %s"
            cursor.execute(sql, (teacher_data['name'], teacher_data['email'], teacher_id))
            conn.commit()
    finally:
        print('ok')

# 查询单个老师
def get_teacher(conn, teacher_id):
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM teachers WHERE id = %s"
            cursor.execute(sql, (teacher_id,))
            teacher = cursor.fetchone()
            return teacher
    finally:
        print('ok')
