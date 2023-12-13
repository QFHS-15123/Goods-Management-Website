import vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '../components/HelloWorld'
import BoxView from '../views/BoxView.vue'


vue.use(Router)


export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/box',
        },
        {
            path: '/box',
            name: 'BoxView',
            component: BoxView
        },
    ]
})
