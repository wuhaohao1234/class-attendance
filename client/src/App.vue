<script setup>

import { useRouter } from 'vue-router';

const router = useRouter();
const goToTeacher = () => {
  router.push('/teacher')
}

const goAcademic = () => {
  router.push('/academic')
}
const goCounselor = () => {
  router.push('/counselor')
}

const goStudent = () => {
  router.push('/leave')
}
</script>

<template>
  <div style="background-image: url(src/assets/bg.png);" >
    <div class="login-page">
      <div class="login-buttons">
        <el-button @click="goStudent">学生</el-button>
        <el-button @click="goCounselor">辅导员</el-button>
        <el-button @click="goAcademic">教务</el-button>
        <!-- <el-button @click="showLogin('teacher')">任课教师</el-button> -->
        <el-button @click="goToTeacher">任课教师</el-button>
      </div>
    </div>

    <router-view></router-view>
  </div>
</template>

<style scoped>
.login-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.login-buttons {
  margin-bottom: 20px;
}

.el-dialog__body {
  padding: 20px;
}
</style>
