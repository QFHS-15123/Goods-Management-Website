const routes = [
    {
        path: '/',
        name: 'Home',
        title: 'Home',
        component: () => import('../views/Home.vue'), //.vue不能省略
    },
    {
        path: '/test',
        name: 'Test',
        title: 'Test',
        component: () => import('../views/TestView.vue'), //.vue不能省略
    },
    // {
    //     path: '/box',
    //     name: 'BoxView',
    //     title: 'BoxView',
    //     component: () => import('../views/Box.vue'), //.vue不能省略
    // },
    // {
    //     path: '/goods',
    //     name: 'HomeView',
    //     title: 'HomeView',
    //     component: () => import('../views/HomeView.vue'), //.vue不能省略
    // },
]
export default routes
