function transformRequest(data) {
    let ret = ''
    for (let it in data) {
      // 防止数据为 null 时，转换成字符串 'null' 传给后端导致报错
      ret += encodeURIComponent(it) + '=' + (data[it] !== null ? encodeURIComponent(data[it]) : '') + '&'
    }
    ret = ret.substring(0, ret.lastIndexOf('&'))
    return ret
}

export default transformRequest
