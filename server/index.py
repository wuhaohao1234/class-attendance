from flask import Flask, jsonify
import pymysql
from student import get_all_students, get_student, add_student, update_student, delete_student

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

if __name__ == '__main__':
    app.run()
