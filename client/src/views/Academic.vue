<template>
  <div class="container pt-10 m-auto">
    <h1 class="text-3xl font-bold mb-4 text-center">管理课程</h1>
    <div class="flex justify-between">
      <h2 class="text-xl font-bold">添加课程</h2>
      <form @submit.prevent="addCourse" class="flex items-center">
        <el-select v-model="newCourse" placeholder="请选择课程" class="mr-4">
          <el-option
            v-for="course in courseOptions"
            :key="course.id"
            :label="course.name"
            :value="course.name"
          ></el-option>
        </el-select>
        <el-button @click="addCourse">添加</el-button>
      </form>
    </div>
    <!-- <h2 class="text-xl font-bold mt-4">课程列表</h2> -->
    <el-table :data="courses" class="mt-2">
      <el-table-column label="课程ID" prop="id"></el-table-column>
      <el-table-column label="课程名称" prop="name"></el-table-column>
      <el-table-column label="操作" align="center">
        <template #default="{ row }">
          <el-button type="text" @click="showAttendance(row)">详情</el-button>
          <!-- <el-button type="text" @click="deleteCourse(row)">删除</el-button> -->
        </template>
      </el-table-column>
    </el-table>
    <el-dialog v-model="attendanceDialogVisible" title="学生出勤" width="400px">
      <ul>
        <li v-for="student in selectedCourseAttendance" :key="student.id">
          {{ student.name }} - {{ student.attendance }}
        </li>
      </ul>
    </el-dialog>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const newCourse = ref("");
    const attendance = ref([]);
    const courseOptions = [
      { id: 1, name: "语文" },
      { id: 2, name: "数学" },
      { id: 3, name: "英语" },
      { id: 4, name: "体育" },
    ];
    const students = ref([])
    const courses = ref();
    const getAttendance = () => {
      return fetch('api/attendance').then(res => res.json()).then(data => {
        attendance.value = data
      });
    }
    const getStudents = () => {
      return fetch('api/students').then(res => res.json()).then(data => {
        students.value = data
      });
    }
    const getCourses = () => {
      return fetch("api/courses")
        .then((res) => res.json())
        .then((data) => {
          courses.value = data;
        });
    }
    getCourses().then(() => {
      return getAttendance()
    }).then(() => {
      return getStudents()
    })

    const selectedCourseAttendance = ref([]);
    const attendanceDialogVisible = ref(false);
    const showAttendance = (course) => {
      const arr = attendance.value.filter(item => {
        return item.course_id === course.id
      })
      selectedCourseAttendance.value = arr.map(item => {
        const obj = students.value.find(student => student.id === item.student_id)
        return {
          name: obj.name,
          attendance: item.status === 1? "出勤" : "未出勤",
        }
      })
      // selectedCourseAttendance.value = course.attendance;
      attendanceDialogVisible.value = true;
    };
    const deleteCourse = (row) => {
        fetch(`api/courses/${row.id}`, {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((res) => res.json())
          .then((data) => {
            getCourses()
            // courses.value = data
          });
    }

    const addCourse = () => {
      if (newCourse.value.trim() !== "") {
        const course = {
          name: newCourse.value,
          teacher_id: 2
        };
        // courses.value.push(course);
        fetch("api/courses", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(course),
        })
          .then((res) => res.json())
          .then((data) => {
            getCourses()
            // courses.value = data
          });
        newCourse.value = "";
      }
    };

    return {
      newCourse,
      courses,
      courseOptions,
      selectedCourseAttendance,
      attendanceDialogVisible,
      addCourse,
      showAttendance,
      deleteCourse
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

.text-center {
  /* 将表格内文本居中 */
}

.mt-2 {
  /* 自定义上边距 */
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
