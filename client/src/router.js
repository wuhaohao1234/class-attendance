import { createRouter, createWebHashHistory } from 'vue-router';
import Home from './views/Home.vue';
import About from './views/About.vue'
import Login from './views/Login.vue'
import Students from './views/Students.vue'
import Teacher from './views/Teacher.vue'
import Academic from './views/Academic.vue'
import Counselor from './views/Counselor.vue'
import Leave from './views/Leave.vue'
const routes = [
  { path: '/', component: Home, redirect: '/login' },
  { path: '/about', component: About },
  {path: '/login', component: Login},
  {path: '/students', component: Students},
  {path: '/teacher', component: Teacher},
  {path: '/teacher', component: Teacher},
  {path: '/academic', component: Academic},
  {path: '/counselor', component: Counselor},
  {path: '/leave', component: Leave},
];
export const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHashHistory(),
  routes, // short for `routes: routes`
});
