-- Create students table
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50)
  -- Other student-related fields
);

-- Create counselors table
CREATE TABLE counselors (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50)
  -- Other counselor-related fields
);

-- Create academic_staff table
CREATE TABLE academic_staff (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50)
  -- Other academic staff-related fields
);

-- Create teachers table
CREATE TABLE teachers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50)
  -- Other teacher-related fields
);

-- Create courses table
CREATE TABLE courses (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  teacher_id INT,
  -- Other course-related fields
  FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

-- Create leaves table
CREATE TABLE leaves (
  id INT PRIMARY KEY,
  student_id INT,
  course_id INT,
  status VARCHAR(20),
  -- Other leave-related fields
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Create attendance table
CREATE TABLE attendance (
  id INT PRIMARY KEY,
  student_id INT,
  course_id INT,
  attendance_date DATE,
  -- Other attendance-related fields
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (course_id) REFERENCES courses(id)
);
