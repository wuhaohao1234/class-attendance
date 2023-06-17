from flask import Flask, jsonify, request
import pymysql
from student import get_all_students, get_student, add_student, update_student, delete_student
from teacher import *
from courses import get_all_courses, add_course, update_course, delete_course
from attendance import create_attendance_record, get_attendance_record, update_attendance_record, delete_attendance_record, get_all_attendance_records
from leaves import get_all_leaves, add_leave, delete_leave, update_leave

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

# 获取所有课程
@app.route('/courses', methods=['GET'])
def get_courses():
    courses = get_all_courses(conn)
    return jsonify(courses)

# 添加课程
@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    name = data['name']
    teacher_id = data['teacher_id']
    course_id = add_course(conn, name, teacher_id)
    return jsonify({'course_id': course_id})

# 更新课程
@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course_route(course_id):
    data = request.get_json()
    name = data['name']
    teacher_id = data['teacher_id']
    update_course(conn, course_id, name, teacher_id)
    return jsonify({'message': 'Course updated successfully'})

# 删除课程
@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course_route(course_id):
    delete_course(conn, course_id)
    return jsonify({'message': 'Course deleted successfully'})

# Create attendance record
@app.route('/attendance', methods=['POST'])
def add_attendance():
    data = request.get_json()
    student_id = data['student_id']
    course_id = data['course_id']
    attendance_date = data['attendance_date']
    status = data['status']

    create_attendance_record(conn, student_id, course_id, attendance_date, status)

    return jsonify({'message': 'Attendance record created successfully'})

# Get attendance record by ID
@app.route('/attendance/<int:attendance_id>', methods=['GET'])
def get_attendance(attendance_id):
    attendance_record = get_attendance_record(conn, attendance_id)

    if attendance_record:
        return jsonify(attendance_record)
    else:
        return jsonify({'message': 'Attendance record not found'}), 404

# Update attendance record
@app.route('/attendance/<int:attendance_id>', methods=['PUT'])
def update_attendance(attendance_id):
    data = request.get_json()
    student_id = data['student_id']
    course_id = data['course_id']
    attendance_date = data['attendance_date']
    status = data['status']

    update_attendance_record(conn, attendance_id, student_id, course_id, attendance_date, status)

    return jsonify({'message': 'Attendance record updated successfully'})

# Delete attendance record
@app.route('/attendance/<int:attendance_id>', methods=['DELETE'])
def delete_attendance(attendance_id):
    delete_attendance_record(conn, attendance_id)

    return jsonify({'message': 'Attendance record deleted successfully'})

# Get all attendance records
@app.route('/attendance', methods=['GET'])
def get_all_attendance():
    attendance_records = get_all_attendance_records(conn)

    return jsonify(attendance_records)

# Get all leaves
@app.route('/leaves', methods=['GET'])
def get_leaves():
    leaves = get_all_leaves(conn)
    return jsonify(leaves)

# Add a leave
@app.route('/leaves', methods=['POST'])
def add_leave_route():
    data = request.get_json()
    student_id = data['student_id']
    course_id = data['course_id']
    status = data['status']
    attendance_date = data['attendance_date']
    print(student_id)
    print(course_id)
    print(attendance_date)
    leave_id = add_leave(conn, student_id, course_id, status)

    return jsonify({'leave_id': leave_id})

# Delete a leave
@app.route('/leaves/<int:leave_id>', methods=['DELETE'])
def delete_leave(leave_id):
    delete_leave(conn, leave_id)

    return jsonify({'message': 'Leave deleted successfully'})

# Update a leave
@app.route('/leaves/<int:leave_id>', methods=['PUT'])
def update_leaver_route(leave_id):
    data = request.get_json()
    student_id = data['student_id']
    course_id = data['course_id']
    status = data['status']

    update_leave(conn, leave_id, student_id, course_id, status)

    return jsonify({'message': 'Leave updated successfully'})

if __name__ == '__main__':
    app.run()
