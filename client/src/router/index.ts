import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Admin from '../components/Admin.vue';
import Users from '../components/Users.vue';

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
    component: Users
  }
];

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});
