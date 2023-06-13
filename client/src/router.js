import { createRouter, createWebHashHistory } from 'vue-router';
import Home from './views/Home.vue';
import About from './views/About.vue'
import Login from './views/Login.vue'
import Students from './views/Students.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  {path: '/login', component: Login},
  {path: '/students', component: Students}
];
export const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHashHistory(),
  routes, // short for `routes: routes`
});
