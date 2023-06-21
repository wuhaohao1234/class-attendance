import pymysql
# 获取所有leave
def get_all_leaves(conn):
    cursor = conn.cursor()
    
    try:
        # 执行查询语句
        cursor.execute("SELECT * FROM leaves")
        
        # 获取查询结果
        leaves = cursor.fetchall()
        return leaves
    finally:
        # 关闭游标，不关闭数据库连接
        # cursor.close()
        print('ok')

# 添加leave
def add_leave(conn, student_id, course_id, status):
    cursor = conn.cursor()
    
    try:
        sql = "INSERT INTO leaves (student_id, course_id, status) VALUES (%s, %s, %s)"
        # 执行插入语句
        cursor.execute(sql, (student_id, course_id, status))
        
        # 提交事务
        conn.commit()
        
        # 获取插入的leaveID
        leave_id = cursor.lastrowid
        return leave_id
    except Exception as e:
        # 发生错误时回滚事务
        conn.rollback()
        raise e
    finally:
        # 关闭游标，不关闭数据库连接
        # cursor.close()

        print('ok')

# 删除leave
def delete_leave(conn, leave_id):
    cursor = conn.cursor()
    
    try:
        # 执行删除语句
        cursor.execute("DELETE FROM leaves WHERE id = %s", (leave_id,))
        
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

# Update leave
def update_leave(conn, leave_id, student_id, course_id, status):
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE leaves SET student_id = %s, course_id = %s, status = %s WHERE id = %s"
            # Execute update statement
            cursor.execute(sql, (student_id, course_id, status,leave_id))

            # Commit the transaction
            conn.commit()
    except Exception as e:
        # Rollback the transaction in case of an error
        conn.rollback()
        raise e

