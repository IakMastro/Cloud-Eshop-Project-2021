import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Ping from '../components/Ping.vue';
import Games from '../components/Games.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
  {
    path: '/',
    name: 'Games',
    component: Games,
  },
];

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});
