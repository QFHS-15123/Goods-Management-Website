const routes = [
    {
        path: '/test',
        name: 'TestView',
        title: 'TestView',
        component: () => import('../views/TestView.vue'), //.vue不能省略
    },{
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
