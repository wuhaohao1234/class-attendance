<script setup>
import { ref } from "vue";
const selectedCourse = ref("");
const courses = ref([]);
const attendance = ref([])

const students = ref([]);

const getCourse = () => {
  return fetch('api/courses').then(res => res.json()).then(data => {
    courses.value = data
  })
}
const getStudents = () => {
  return fetch('api/students').then(res => res.json()).then(data => {
    students.value = data
  });
}

const getAttendance = () => {
  return fetch('api/attendance').then(res => res.json()).then(data => {
    attendance.value = data
  });
}

getCourse().then(() => {
  return getStudents()
}).then(() => {
  getAttendance()
})

const updateAttendance = (courseId, studentId, status) => {
  const attendanceObj = {
    student_id: studentId, course_id: courseId, attendance_date: new Date(), status: status
  }
  return fetch('api/attendance', {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(attendanceObj),
  }).then(res => res.json()).then(data => {
    selectedCourse.value = ''
    getStudents().then(() => {
      getAttendance()
    })
  });
}

const handleAttendance = (row) => {
  if(selectedCourse.value === ""){
    return
  }
  updateAttendance(selectedCourse.value, row.id, 1)
}
const absenceFromWork = (row) => {
  if(selectedCourse.value === ""){
    return
  }
  updateAttendance(selectedCourse.value, row.id, 2)
}

const handleSelectedCourse = async () => {
  // console.log(attendance.value[0].course_id)
  await getStudents()
  if(attendance.value.length === 0) {
    return
  }
  const arr = attendance.value.filter(item => item.course_id === selectedCourse.value)
  if(arr.length > 0){
    const newArr = students.value.map(item => {
      arr.forEach((obj, key) => {
        if(item.id === obj.student_id){
          console.log(obj);
          item.status = obj.status
        }
      })
      return item
    })
    students.value = []
    console.log(newArr);
    students.value = newArr.map(item => item)
  }
}

const submit = () => {};
</script>
<template>
  <div class="container pt-10 m-auto container pt-10 m-auto h-screen" >
    <h1 class="text-center text-3xl pb-5" >学生考勤</h1>
    <div class="select-class flex justify-between">
      <div>
        <el-select v-model="selectedCourse" @change="handleSelectedCourse" class="mr-5" placeholder="请选择课程">
          <el-option
            v-for="course in courses"
            :key="course.id"
            :label="course.name"
            :value="course.id"
          ></el-option>
        </el-select>
      </div>
      <el-button class="add-student-btn" @click="submit">提交</el-button>
    </div>
    <el-table :data="students" border>
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="email" label="学号"></el-table-column>
      <el-table-column label="操作">
        <template #default="{row}">
          <el-button v-if="!row.status" type="text" @click="handleAttendance(row)" >出勤</el-button>
          <el-button v-if="!row.status" type="text" @click="absenceFromWork(row)" >缺勤</el-button>
          <span v-if="row.status === 1" >出勤</span>
          <span v-if="row.status === 2" >缺勤</span>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
