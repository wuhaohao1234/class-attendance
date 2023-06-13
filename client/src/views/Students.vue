<template>
  <div class="student-page">
    <el-button class="add-student-btn" @click="handleAddStudent">添加学生</el-button>

    <el-table :data="students" border>
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="age" label="年龄"></el-table-column>
      <el-table-column label="操作">
        <template #default="{ row }">
          <el-button type="text" @click="handleShowAttendanceDialog(row)">查看考勤</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog v-model="showAddStudentDialog" title="添加学生">
      <el-form :model="newStudent" label-width="80px">
        <el-form-item label="姓名">
          <el-input v-model="newStudent.name"></el-input>
        </el-form-item>
        <el-form-item label="年龄">
          <el-input-number v-model="newStudent.age" controls-position="right"></el-input-number>
        </el-form-item>
        <el-form-item>
          <el-button @click="addStudent">确认添加</el-button>
          <el-button @click="cancelAddStudent">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>

    <el-dialog v-model="showAttendanceDialog" :title="currentStudent.name + '的考勤'">
      <el-table :data="currentStudent.attendance" border>
        <el-table-column prop="date" label="日期"></el-table-column>
        <el-table-column prop="status" label="状态"></el-table-column>
      </el-table>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const students = ref([
  { name: '学生1', age: 18, attendance: [{ date: '2023-06-01', status: '出勤' }, { date: '2023-06-02', status: '缺勤' }] },
  { name: '学生2', age: 19, attendance: [{ date: '2023-06-01', status: '缺勤' }, { date: '2023-06-02', status: '出勤' }] },
  { name: '学生2', age: 19, attendance: [{ date: '2023-06-01', status: '缺勤' }, { date: '2023-06-02', status: '出勤' }] },
]);

const showAttendanceDialog = ref(false);

const newStudent = ref({
  name: '',
  age: 0,
});

const currentStudent = ref({
  name: '',
  attendance: [],
});

const showAddStudentDialog = ref(false)

const handleAddStudent = () => {
  showAddStudentDialog.value = true;
};

const cancelAddStudent = () => {
  showAddStudentDialog.value = false;
  newStudent.value.name = '';
  newStudent.value.age = 0;
};

const addStudent = () => {
  students.value.push({
    name: newStudent.value.name,
    age: newStudent.value.age,
    attendance: [],
  });
  cancelAddStudent();
};

const handleShowAttendanceDialog = (student) => {
  currentStudent.value = {
    name: student.name,
    attendance: student.attendance,
  };
  showAttendanceDialog.value = true;
};
</script>

<style>
.student-page {
  padding: 20px;
}

.add-student-btn {
  margin-bottom: 20px;
}
</style>
