import service from '../utils/axios_config'
import transformRequest from '../utils/transformRequest'


export default {
    // login(user){
    //     return service({
    //         url: '/',
    //         method: 'get',
    //         // data: transformRequest(user),
    //         // headers: {
    //         //     'Content-Type': 'application/x-www-form-urlencoded'
    //         // }
    //     })
    // },
    get_all_boxes(){
        return service({
            url: '/box',
            method: 'get',
        })
    },
    get_all_goods(boxName) {
        return service({
            url: '/goods?box_name=' + boxName,
            method: 'get',
            headers: {
                'Content-Type': 'application/json'
            }
        })
    },
    add_box(newBox) {
        return service({
            url: '/box/addBox',
            method: 'post',
            data: newBox,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }
}
