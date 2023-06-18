<template>
  <div class="container pt-10 m-autoi container pt-10 m-auto h-screen">
    <h1 class="text-3xl font-bold mb-4">请假申请</h1>

    <el-form ref="leaveForm" :model="leaveRequest" label-width="120px" class="mt-4" @submit.native.prevent="submitLeaveRequest">
      <!-- <el-form-item label="学生姓名" prop="studentName">
        <el-input v-model="leaveRequest.studentName" placeholder="请输入学生姓名" clearable></el-input>
      </el-form-item> -->
      <el-form-item label="请假日期" prop="leaveDate">
        <el-date-picker v-model="leaveRequest.leaveDate" type="date" placeholder="请选择请假日期"></el-date-picker>
      </el-form-item>
      <el-form-item label="请假课程" prop="course">
        <el-select v-model="leaveRequest.course" placeholder="请选择请假课程">
          <el-option v-for="course in courses" :key="course.id" :label="course.name" :value="course.id"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="学生" prop="course">
        <el-select v-model="leaveRequest.studentName" @change="selectStudent"  placeholder="请选择请假课程">
          <el-option v-for="student in students" :key="student.id" :label="student.name" :value="student.id"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" native-type="submit">提交请假申请</el-button>
      </el-form-item>
    </el-form>
    <el-table :data="courses" class="mt-2">
      <el-table-column label="课程ID" prop="id"></el-table-column>
      <el-table-column label="课程名称" prop="name"></el-table-column>
      <el-table-column label="操作" align="center">
        <template #default="{ row}">
          <!-- <el-button type="text" @click="showAttendance(row)">详情</el-button> -->
          <span v-show="row.id % 2 === 1">缺勤</span>
          <span v-show="row.id % 2 === 0">出勤</span>
          <!-- <el-button type="text" @click="deleteCourse(row)">删除</el-button> -->
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { ElMessage } from 'element-plus'
import { h } from 'vue'
export default {
  setup() {
    const router = useRouter()
    const leaveRequest = ref({
      studentName: '',
      leaveDate: '',
      course: '',
    });
    const courses = ref([]);
    const students = ref([]);
    const getCourses = () => {
      return fetch("api/courses")
        .then((res) => res.json())
        .then((data) => {
          courses.value = []
          setTimeout(() => {
            courses.value = data;
          }, 500);
        });
    }
    const getStudents = () => {
      fetch('api/students').then(res => res.json()).then(data => {
        students.value = data
      });
    }
    getCourses().then(() => {
      getStudents()
    })
    const addLeaves = (leaveRequest) => {
      fetch('api/leaves', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(leaveRequest),
      }).then(res => res.json()).then(data => {
        // router.push('/counselor')
        // students.value = data
        ElMessage({
          message: h('p', null, [
            h('span', null, '申请成功'),
          ]),
        })
      });
    }
    const selectStudent = () => {
      getCourses()
    }

    const submitLeaveRequest = () => {
          // 在这里执行提交请假申请的逻辑，例如通过 API 发送请求保存请假申请到后端数据库
          console.log(leaveRequest.value);
          // 重置表单字段
          const leave = {
            student_id: leaveRequest.value.studentName,
            course_id: leaveRequest.value.course,
            attendance_date: leaveRequest.value.leaveDate.toString().split(0, 20),
            teacher_id: 2,
            status: '申请中',
          };
          addLeaves(leave)
    };

    return {
      leaveRequest,
      courses,
      students,
      selectStudent,
      submitLeaveRequest
    };
  }
};
</script>
