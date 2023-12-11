import vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld'


vue.use(Router)


export default new Router({
  routes: [
    {                    //每一个链接都是一个对象
        path: '/',         //链接路径
        name: 'HelloWorld',     //路由名称，
        component: HelloWorld   //对应的组件模板
    }
  ]
})
