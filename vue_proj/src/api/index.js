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
    getAllBoxes(){
        return service({
            url: '/box',
            method: 'get',
        })
    },
    getAllGoods(boxName) {
        return service({
            url: '/goods/?box_name=' + boxName,
            method: 'get',
            headers: {
                'Content-Type': 'application/json'
            }
        })
    },
    deleteItem(mode, name){
        return service({
            url: '/del?mode=' + mode + '&name=' + name,
            method: 'get'
        })
    },
    permanentlyDelete(mode, name){
    return service({
        url: '/permanentlyDel?mode=' + mode + '&name=' + name,
        method: 'get'
    })
    },
    addItem(newItem) {
        return service({
            url: '/add',
            method: 'post',
            data: newItem,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }
}
