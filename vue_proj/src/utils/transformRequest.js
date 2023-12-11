function transformRequest(data) {
    let ret = ''
    for (let it in data) {
      ret += encodeURIComponent(it) + '=' + (data[it] !== null ? encodeURIComponent(data[it]) : '') + '&'
    }
    ret = ret.substring(0, ret.lastIndexOf('&'))
    return ret
}

export default transformRequest
