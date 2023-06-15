<template>
  <div class="container mt-10 m-auto">
    <h1 class="text-3xl font-bold mb-4">请假申请</h1>

    <el-form ref="leaveForm" :model="leaveRequest" label-width="120px" class="mt-4" @submit.native.prevent="submitLeaveRequest">
      <el-form-item label="学生姓名" prop="studentName">
        <el-input v-model="leaveRequest.studentName" placeholder="请输入学生姓名" clearable></el-input>
      </el-form-item>
      <el-form-item label="请假日期" prop="leaveDate">
        <el-date-picker v-model="leaveRequest.leaveDate" type="date" placeholder="请选择请假日期"></el-date-picker>
      </el-form-item>
      <el-form-item label="请假课程" prop="course">
        <el-select v-model="leaveRequest.course" placeholder="请选择请假课程">
          <el-option v-for="course in courses" :key="course.id" :label="course.name" :value="course.id"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="请假原因" prop="reason">
        <el-input type="textarea" v-model="leaveRequest.reason" placeholder="请输入请假原因" rows="4"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button native-type="submit">提交请假申请</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const leaveRequest = ref({
      studentName: '',
      leaveDate: '',
      course: '',
      reason: ''
    });

    const courses = [
      { id: 1, name: '数学' },
      { id: 2, name: '英语' },
      { id: 3, name: '物理' }
    ];

    const submitLeaveRequest = () => {
      this.$refs.leaveForm.validate((valid) => {
        if (valid) {
          // 在这里执行提交请假申请的逻辑，例如通过 API 发送请求保存请假申请到后端数据库
          console.log(leaveRequest.value);
          // 重置表单字段
          leaveRequest.value = {
            studentName: '',
            leaveDate: '',
            course: '',
            reason: ''
          };
        }
      });
    };

    return {
      leaveRequest,
      courses,
      submitLeaveRequest
    };
  }
};
</script>
