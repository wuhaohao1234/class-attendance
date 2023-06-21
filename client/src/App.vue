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
  <div style="" >
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
.el-button {
  /* padding-top: 20px; */
  color: #000;
  background: #fff;
  font-size: 1.4rem;
  font-weight: bold;
}
</style>
