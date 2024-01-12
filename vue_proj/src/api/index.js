import service from '../utils/axios_config'
import transformRequest from '../utils/transformRequest'


export default {
    openBox() {
        return service({
            url: '/open_box',
            method: 'get',
        })
    },
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
    restoreItem(mode, name){
        return service({
            url: '/restore?mode=' + mode + '&name=' + name,
            method: 'get'
        })
    },
    addBox(newBox) {
        return service({
            url: '/box/add',
            method: 'post',
            data: newBox,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    },
    addGoods(newGoods) {
        return service({
            url: '/goods/add',
            method: 'post',
            data: newGoods,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    },
    updateGoods(boxName, goodsName, col, value, updateTime) {
        return service({
            url: '/goods/update?box_name=' + boxName + '&goods_name=' + goodsName + '&col=' + col + '&value=' + value
                + '&update_time=' + updateTime,
            method: 'get'
        })
    },
    updateBox(name, value, updatedTime) {
        return service({
            url: '/box/update?name=' + name + '&value=' + value + '&updated_time=' + updatedTime,
            method: 'get'
        })
    }
}
