import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Ping from '../components/Ping.vue';
import Admin from '../components/Admin.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
  {
    path: '/',
    name: 'Admin',
    component: Admin,
  },
];

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});
