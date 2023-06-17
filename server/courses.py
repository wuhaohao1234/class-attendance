
import pymysql
# 获取所有课程
def get_all_courses(conn):
    cursor = conn.cursor()
    
    try:
        # 执行查询语句
        cursor.execute("SELECT * FROM courses")
        
        # 获取查询结果
        courses = cursor.fetchall()
        return courses
    finally:
        # 关闭游标，不关闭数据库连接
        # cursor.close()
        print('ok')

# 添加课程
def add_course(conn, name, teacher_id):
    cursor = conn.cursor()
    
    try:
        # 执行插入语句
        cursor.execute("INSERT INTO courses (name, teacher_id) VALUES (%s, %s)", (name, teacher_id))
        
        # 提交事务
        conn.commit()
        
        # 获取插入的课程ID
        course_id = cursor.lastrowid
        return course_id
    except Exception as e:
        # 发生错误时回滚事务
        conn.rollback()
        raise e
    finally:
        # 关闭游标，不关闭数据库连接
        # cursor.close()

        print('ok')

# 更新课程
def update_course(conn, course_id, name, teacher_id):
    cursor = conn.cursor()
    
    try:
        # 执行更新语句
        cursor.execute("UPDATE courses SET name = %s, teacher_id = %s WHERE id = %s", (name, teacher_id, course_id))
        
        # 提交事务
        conn.commit()
    except Exception as e:
        # 发生错误时回滚事务
        conn.rollback()
        raise e
    finally:
        # 关闭游标，不关闭数据库连接
        print('ok')
        # cursor.close()

# 删除课程
def delete_course(conn, course_id):
    cursor = conn.cursor()
    
    try:
        # 执行删除语句
        cursor.execute("DELETE FROM courses WHERE id = %s", (course_id,))
        
        # 提交事务
        conn.commit()
    except Exception as e:
        # 发生错误时回滚事务
        conn.rollback()
        raise e
    finally:
        # 关闭游标，不关闭数据库连接
        print('ok')
        # cursor.close()
