import Vue from 'vue';
import Router from 'vue-router';
// import Home from './views/Home.vue';

const routerOption = [
  {
    path: '/',
    component: 'Books',
    name: 'Books',
  },
];

// eslint-disable-next-line no-undef
const routes = routerOption.map(route => ({
  ...route,
  component: () => import(`@/views/${route.component}.vue`),
}));

Vue.use(Router);

export default new Router({
  routes,
  mode: 'history',
});
