# Initialize
## Back End (Flask)
### Introduction to Flask
Initialize a flask project in PyCharm.
#### Most Simple Example
```Python
from flask import Flask, escape, request  
  
app = Flask(__name__)  
  
  
@app.route('/')  
def hello_world():  # put application's code here  
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


@app.route('/login', methods=['POST', 'GET'])  
def login():  
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
    /__init__.py
    /templates
        /hello.html
```
```html
<!--hello.html-->
<title>Hello from Flask</title>  
{% if error %}  
  <h1>An error: {{ error }}!</h1>  
{% else %}  
  <h1>Hello, World!</h1>  
{% endif %}
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
#### Serve CORS
Install flask-cors
Global:
```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
```
For each function:
```python	
@cross_origin(supports_credentials=True)
```
## Front End (Flask)
### Prepare Environment and Initialize a Project
1. Install [Node.js](https://nodejs.org/en/download/)
2. IDEA create a Vite Project
3. Run. Default  Local:   http://localhost:5173/
4. Install element-plus
	```js
		import ElementPlus from "// main.js
element-plus";
	
	createApp(App)
		...
	    .use(ElementPlus)
	    ...
	```
### Prepare Api
#### Initialize Vue File

```vue
<!--HelloWorld.vue-->
<script setup name="HelloWorld">
...
const user = {}
...
</script>

<template>
<div><el-button type="primary">A Lonely Button</el-button></div>
<div>Username: {{ user.username }}</div>  
<div>Password: {{ user.password }}</div>
</div>
</template>
```
#### Set Proxy
[vue3新语法糖——setup script - 掘金 (juejin.cn)](https://juejin.cn/post/6944190150406570020)
```js
// vite.config.js
export default defineConfig({  
  ...,
  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:5000",
        changOrigin: true,
        pathRewrite: {
          '^/api': '/'
        }
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

createApp(App)
	...
    .use(VueAxios, axios)
    ...
const app = createApp(App)  
app.config.globalProperties.$axios = axios;
```
```vue
<!--HelloWorld.vue-->
<script setup name="HelloWorld">
...
import { getCurrentInstance, onBeforeMount, ...} from "vue";  
  
let { proxy } = getCurrentInstance();  
  
onBeforeMount(() => {  
  proxy.$http  
    .post("/api/user/info", {  
      user: "QFHS",  
      password: "15123",  
    })  
    .then(function(res) {  
      console.log(res.user)  
    })  
    .catch(function(error) {  
      console.log(error);  
    });  
});
...
</script>
```

# Connect Database
