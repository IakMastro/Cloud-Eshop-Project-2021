import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Admin from '../components/Admin.vue';
import Users from '../components/Users.vue';
import Library from '../components/Library.vue';
import Login from '../components/Login.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '/admin',
    name: 'Admin',
    component: Admin,
  },
  {
    path: '/login',
    name: 'Users',
    component: Users,
  },
  {
    path: '/library',
    name: 'Library',
    component: Library,
  },
];

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});
