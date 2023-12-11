import service from '../utils/axios_config'
import transformRequest from '../utils/transformRequest'

const api_name = 'api'

export default {
    login(user){
        return service({
            url: '/login',
            method: 'post',
            data: transformRequest(user),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        })
    }
}
