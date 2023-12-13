import service from '../utils/axios_config'
import transformRequest from '../utils/transformRequest'


export default {
    login(user){
        return service({
            url: '/',
            method: 'get',
            // data: transformRequest(user),
            // headers: {
            //     'Content-Type': 'application/x-www-form-urlencoded'
            // }
        })
    },
    get_all_boxes(){
        return service({
            url: '/box',
            method: 'get',
        })
    },
}
