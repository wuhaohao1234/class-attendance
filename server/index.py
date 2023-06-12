from flask import Flask, jsonify, request
import pymysql
from student import get_all_students, get_student, add_student, update_student, delete_student
from teacher import *

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'  # 数据库主机名
app.config['MYSQL_USER'] = 'root'  # 数据库用户名
app.config['MYSQL_PASSWORD'] = 'abu0418'  # 数据库密码
app.config['MYSQL_DB'] = 'attendance_system'  # 数据库名称

# 创建MySQL连接
conn = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB'],
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/students', methods=['GET'])
def get_all_students_route():
    students = get_all_students(conn)
    return jsonify(students)

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_route(student_id):
    student = get_student(conn, student_id)
    return jsonify(student)

@app.route('/students', methods=['POST'])
def add_student_route():
    data = request.get_json()
    name = data['name']
    email = data['email']
    print(name)
    print(email)
    result = add_student(conn, name, email)
    return jsonify(result)

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student_route(student_id):
    data = request.get_json()
    name = data['name']
    email = data['email']
    result = update_student(conn, student_id, name, email)
    return jsonify(result)

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student_route(student_id):
    result = delete_student(conn, student_id)
    return jsonify(result)

# 路由 - 获取所有老师
@app.route('/teachers', methods=['GET'])
def get_all_teachers_route():
    teachers = get_all_teachers(conn)
    return jsonify(teachers)

# 路由 - 添加老师
@app.route('/teachers', methods=['POST'])
def add_teacher_route():
    teacher_data = request.get_json()
    add_teacher(conn, teacher_data)
    return jsonify({'message': 'Teacher added successfully'})

# 路由 - 删除老师
@app.route('/teachers/<int:teacher_id>', methods=['DELETE'])
def delete_teacher_route(teacher_id):
    delete_teacher(conn, teacher_id)
    return jsonify({'message': 'Teacher deleted successfully'})

# 路由 - 更新老师
@app.route('/teachers/<int:teacher_id>', methods=['PUT'])
def update_teacher_route(teacher_id):
    teacher_data = request.get_json()
    update_teacher(conn, teacher_id, teacher_data)
    return jsonify({'message': 'Teacher updated successfully'})

# 路由 - 查询单个老师
@app.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher_route(teacher_id):
    teacher = get_teacher(conn, teacher_id)
    return jsonify(teacher)

if __name__ == '__main__':
    app.run()
