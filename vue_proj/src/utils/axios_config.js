import axios from 'axios'

const service = axios.create({
    baseURL: 'http://localhost:5000',
    timeout: 30000
})

export default service
