const routes = [
    {
        path: '/box',
        name: 'BoxView',
        title: 'BoxView',
        component: () => import('../views/BoxView.vue'), //.vue不能省略
    }
]
export default routes
