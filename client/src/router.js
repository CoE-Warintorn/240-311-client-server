import Vue from 'vue';
import Router from 'vue-router';

const routerOption = [
  {
    path: '/',
    name: 'Books',
    component: 'Books',
  },
  {
    path: '/about',
    name: 'About',
    component: 'About',
  },
];

const routes = routerOption.map(route => ({
  ...route,
  component: () => import(`@/views/${route.component}.vue`),
}));

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});
