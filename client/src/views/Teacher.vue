<script setup>
import { ref } from "vue";
const selectedCourse = ref("");
const courses = ref([]);


const students = ref([]);

const getCourse = () => {
  fetch('api/courses').then(res => res.json()).then(data => {
    courses.value = data
  })
}

getCourse()

const getStudents = () => {
  fetch('api/students').then(res => res.json()).then(data => {
    students.value = data
  });
}

setTimeout(() => {
  getStudents()
}, 500);



const submit = () => {};
</script>
<template>
  <div class="container mt-10 m-auto" >
    <h1 class="text-center text-3xl pb-5" >学生考勤</h1>
    <div class="select-class flex justify-between">
      <div>
        <el-select v-model="selectedCourse" class="mr-5" placeholder="请选择课程">
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
      <el-table-column prop="email" label="email"></el-table-column>
      <el-table-column label="操作">
        <template #default="">
          <el-button type="text">出勤</el-button>
          <el-button type="text">缺勤</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
