const routes = [
    {
        path: '/box',
        name: 'BoxView',
        title: 'BoxView',
        component: () => import('../views/BoxView.vue'), //.vue不能省略
    },
    {
        path: '/goods',
        name: 'GoodsView',
        title: 'GoodsView',
        component: () => import('../views/GoodsView.vue'), //.vue不能省略
    },
]
export default routes
