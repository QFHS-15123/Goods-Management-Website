
# Initialize  
## Back End (Flask)  
### Introduction to Flask  
Initialize a flask project in PyCharm.  
#### Most Simple Example  
```Python  
from flask import Flask, escape, request    
 app = Flask(__name__)    
    
 @app.route('/') def hello_world():  # put application's code here    
return 'Hello World!'   
  
if __name__ == '__main__':    
    app.run()  
```  
  
Default site is http://127.0.0.1:5000. Visit it to check your progress.  
  
#### Http in Flask  
Get: Front want something from Back.  
Post: Front send something to Back.  
##### Code  
```python  
# __init__.py  
def valid_login(param, param1):    
    return 1    
    
 def log_the_user_in(param):    
print('User login: ' + str(param))   
  
@app.route('/login', methods=['POST', 'GET']) def login():    
    error = None    
 if request.method == 'POST':    
        if valid_login(request.form['username'],    
                       request.form['password']):    
            log_the_user_in(request.form['username'])    
        else:    
            error = 'Invalid username/password'    
  # the code below is executed if the request method was GET or the credentials were invalid    
  return render_template('hello.html', error=error)  
```  
Don't forget to create template hello.html  
```  
/yourapplication  
 /__init__.py /templates /hello.html```  
```html  
<!--hello.html-->  
<title>Hello from Flask</title> {% if error %}    
<h1>An error: {{ error }}!</h1> {% else %}    
<h1>Hello, World!</h1> {% endif %}  
```  
##### Test  
Test in [PostMan](https://www.postman.com/downloads/?_sm_byp=iVVj3HsMQRFr4rFM)  
Post: http://127.0.0.1:5000/login  
###### Normal  
Add a form-data as Body:   
|Key|Value|  
|---|---|  
|username|QFHS|  
|password|15123|  
Click Push button and check the response:  
```html  
<title>Hello from Flask</title>  
<h1>Hello, World!</h1>  
```  
###### Invalid  
Add a form-data as Body:   
|Key|Value|  
|---|---|  
|username|QFHS|  
Response:  
```html  
<!doctype html>  
<html  lang=en>  
<title>400 Bad Request</title>  
<h1>Bad Request</h1>  
<p>The browser (or proxy) sent a request that this server could not understand.</p>  
```  
#### Solve CORS 
Install flask-cors  

For each function:  
```python 
res = make_response(render_template('hello.html', error=error))  
res.status = '200'  
res.headers['Access-Control-Allow-Origin'] = "*"  
res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'  
```  
## Front End (Vue)  
### Prepare Environment and Initialize a Project  
1. Install [Node.js](https://nodejs.org/en/download/)  
2. IDEA create a Vite Project  
3. Run. Default  Local:   http://localhost:5173/  
4. Install element-plus  
    ```js  
    import ElementPlus from "// main.js  
element-plus";  
      
 createApp(App) ... .use(ElementPlus) ... ```### Prepare Api  
#### Set Proxy 
```js  
// vite.config.js  
export default defineConfig({
  ...,
  devServer: {
    proxy: {
      '/api': {
        target: "http://localhost:5000/",
        changOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, "")
      }
    }
  }
})
```  
#### Install axios  
```js  
// main.js  
import VueAxios from 'vue-axios'  
import axios from "axios"  

const app = createApp(App).use(VueAxios, axios)...
app.config.globalProperties.$axios = axios
...
```
```js
// src/utils/axios_config.js
import axios from 'axios'

const service = axios.create({
  baseURL: 'http://localhost:5000',
  timeout: 30000
})

export default service
```
#### Set Api
```js
// src/utils/transformRequest.js
function transformRequest(data) {
  let ret = ''
  for (let it in data) {
    ret += encodeURIComponent(it) + '=' + (data[it] !== null ? encodeURIComponent(data[it]) : '') + '&'
  }
  ret = ret.substring(0, ret.lastIndexOf('&'))
  return ret
}

export default transformRequest
```
```js
// src/api/index.js
import service from '../utils/axios_config'
import transformRequest from '../utils/transformRequest'

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
```
```vue
<!--src/components/HelloWorld.vue-->  
<script setup name="HelloWorld">
import userApi from '../api/index'
import { onBeforeMount } from "vue"

const user = {  
  username: "QFHS",  
  password: "15123",  
}

onBeforeMount(() => {
  userApi.login(user)
    .then(res =>{
    console.log(res.data)
    })
});  
</script>

<template>
<div>Username: {{ user.username }}</div>
<div>Password: {{ user.password }}</div>
</template>
```  
  
# Flask <-> SQLite
