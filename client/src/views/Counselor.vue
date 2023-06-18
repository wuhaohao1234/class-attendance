<template>
  <div class="container pt-10 m-auto h-screen">
    <h1 class="text-3xl font-bold mb-4 text-center">学生出勤</h1>

    <!-- <Teacher /> -->
    <el-table :data="students" class="mt-5" border>
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="email" label="email"></el-table-column>
      <el-table-column label="请假情况">
        <template #default="{row}">
          <span >否</span>
        </template>
      </el-table-column>
      <el-table-column label="考勤">
        <template #default="{row}">
          <span >缺勤</span>
        </template>
      </el-table-column>
    </el-table>

    <h1 class="text-3xl font-bold mb-4 mt-10 text-center">请假审批</h1>
    <el-table :data="leaveRequests" border class="mt-2">
      <el-table-column
        label="学生姓名"
        prop="studentName"
        align="center"
      ></el-table-column>

      <el-table-column
        label="请假课程"
        prop="course"
        align="center"
      ></el-table-column>

      <el-table-column label="操作" align="center">
        <template #default="{ row }">
          <el-button size="mini" @click="approveLeave(row)">批准</el-button>
          <el-button size="mini" @click="rejectLeave(row)">拒绝</el-button>
          <!-- <span v-else>{{ row.status }}</span> -->
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  components: {
    Teacher: () => import("./Teacher.vue"),
  },
  setup() {
    // const leaveRequests = ref([
    //   { id: 1, studentName: '学生1', leaveDate: '2023-06-15', course: '数学', reason: '家庭原因', status: 'pending' },
    //   { id: 2, studentName: '学生2', leaveDate: '2023-06-16', course: '英语', reason: '病假', status: 'approved' },
    //   { id: 3, studentName: '学生3', leaveDate: '2023-06-17', course: '物理', reason: '事假', status: 'rejected' }
    // ]);
    const leaveRequests = ref([]);
    const students = ref([])
    const courses = ref([])
    const getLeaves = () => {
      return fetch("api/leaves")
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          console.log(students.value);
          data.map(item => {
            item.studentName = students.value.find(student => student.id === item.student_id).name
            item.course = courses.value.find(course => course.id === item.course_id).name
            return item
          })
          // students.value = data
          leaveRequests.value = data;
        });
    };
    const getCourses = () => {
      return fetch("api/courses")
        .then((res) => res.json())
        .then((data) => {
          courses.value = data;
        });
    }
    const getStudents = () => {
      return fetch("api/students")
        .then((res) => res.json())
        .then((data) => {
          students.value = data;
        });
    };
    getCourses().then(() => getStudents().then(() => getLeaves()));
    const approveLeave = (row) => {
      row.status = "approved";
    };

    const rejectLeave = (row) => {
      row.status = "rejected";
    };

    return {
      leaveRequests,
      students,
      approveLeave,
      rejectLeave,
    };
  },
};
</script>

<style>
/* 使用Tailwind CSS的样式 */
.flex {
  /* 使用 flex 类将容器内的元素水平居中 */
}

.items-center {
  /* 使用 items-center 类将容器内的元素垂直居中 */
}

/* 自定义Element UI的表格样式 */
.el-table {
  width: 100%;
}

.el-table__header th {
  text-align: center;
}

.el-table__body td {
  text-align: center;
}
</style>
