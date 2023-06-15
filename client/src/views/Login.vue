<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const showDialog = ref(false)
const currentRole = ref('')
const studentForm = ref({
  studentId: '',
  password: ''
})
const counselorForm = ref({
  employeeId: '',
  password: ''
})
const router = useRouter();
const showLogin = (role) => {
  showDialog.value = true
  currentRole.value = role
}
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
  <div class="login-page">
    <h1 class="font-bold text-2xl pb-5" >考勤管理系统</h1>
    <div class="login-buttons">
      <el-button @click="goStudent">学生</el-button>
      <el-button @click="goCounselor">辅导员</el-button>
      <el-button @click="goAcademic">教务</el-button>
      <!-- <el-button @click="showLogin('teacher')">任课教师</el-button> -->
      <el-button @click="goToTeacher">任课教师</el-button>
    </div>

    <el-dialog v-model="showDialog" :title="currentRole + ' 登录'">
      <!-- 根据角色渲染相应的登录表单 -->
      <el-form v-if="currentRole === 'student'" :model="studentForm" label-width="80px">
        <el-form-item label="学号">
          <el-input v-model="studentForm.studentId"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="studentForm.password" type="password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button>登录</el-button>
        </el-form-item>
      </el-form>

      <el-form v-else-if="currentRole === 'counselor'" :model="counselorForm" label-width="80px">
        <el-form-item label="工号">
          <el-input v-model="counselorForm.employeeId"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="counselorForm.password" type="password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button>登录</el-button>
        </el-form-item>
      </el-form>

      <!-- 教务和任课教师的登录表单类似，省略代码 -->

    </el-dialog>
  </div>
</template>



<style>
.login-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.login-buttons {
  margin-bottom: 20px;
}

.el-dialog__body {
  padding: 20px;
}
</style>
