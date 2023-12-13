# Initialize
## Initialize Back End (Flask)
Initialize a flask project in PyCharm.
### Most Simple Example
```Python
# app.py
import os
from flask import Flask

def create_app(test_config=None):
  # create and configure the app app = Flask(__name__, instance_relative_config=True)
  # a simple page that says hello @app.route('/hello') def hello(): return 'Hello, World!'
  return app
```
Run/Debug Configurations:
|Target type|Script path|
|--|--|
|Target|... /app.py|
|Application|create_app|
|Additional options|--port=5000|
|FLASK_ENV|development|

The application run at http://127.0.0.1:5000. Visit to check your progress.

### Http in Flask
Get: Front want something from Back.
Post: Front send something to Back.
```python 
# app.py 
@app.route('/login', methods=['POST', 'GET'])
def login():
  error = None
  if request.method == 'POST':
    if valid_login(request.form['username'], request.form['password']):
      log_the_user_in(request.form['username'])
    else:
      error = 'Invalid username/password'
  # the code below is executed if the request method was GET or the credentials were invalid
return render_template('hello.html', error=error) 
```
Don't forget to create the template `hello.html`
```html
<!--/templates/hello.html-->
<title>Hello from Flask</title>
{% if error %}
<h1>An error: {{ error }}!</h1>
{% else %}
<h1>Hello, World!</h1>
{% endif %} 
```
Test in [PostMan](https://www.postman.com/downloads/?_sm_byp=iVVj3HsMQRFr4rFM)
Post: http://127.0.0.1:5000/login ###### Normal
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
Test invalid request:
Add a form-data as Body: 
|Key|Value|
|---|---|
|username|QFHS|
Response:
```html 
<!doctype html> <html  lang=en> 
<title>400 Bad Request</title> 
<h1>Bad Request</h1> 
<p>The browser (or proxy) sent a request that this server could not understand.</p> 
```
### Solve CORS 
Install flask-cors

For each function:
```python 
res = make_response(render_template('hello.html', error=error))
res.status = '200'
res.headers['Access-Control-Allow-Origin'] = "*"
res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
```
## Initialize Front End (Vue)
### Prepare Environment and Initialize a Project
1. Install [Node.js](https://nodejs.org/en/download/)
2. IDEA create a Vite Project
3. Run. Default  Local:   http://localhost:5173/ 4. Install element-plus
```js
// main.js
import ElementPlus from " element-plus";

createApp(App)
  ...
  .use(ElementPlus)
  ... 
```
### Prepare Api
#### Set Proxy 
```js 
// vite.config.js 
import { defineConfig } from 'vite'  
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
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
import VueAxios from 'vue-axios' import axios from "axios" 

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
      url: '/box',
      method: 'get',
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
## Bluprint in Flask
```py
# box.py
from flask import Blueprint

bp = Blueprint('box', __name__, url_prefix='/box')

@bp.route('/', methods=['GET', 'POST'])  
def get_all_boxes():
  ...
```
Register in application:
```py
# app.py
import box  
app.register_blueprint(box.bp)
```
## Flask <-> SQLite
[ Flask official tutorial](https://flask.palletsprojects.com/en/3.0.x/tutorial/database/)
### Connect to Database
```py
# db.py
import sqlite3
from flask import current_app, g

def get_db():
  if 'db' not in g:
    g.db = sqlite3.connect(
      current_app.config['DATABASE'],
      detect_types=sqlite3.PARSE_DECLTYPES
    )
    g.db.row_factory = sqlite3.Row

  return g.db


def close_db(e=None):
  db = g.pop('db', None)

  if db is not None:
    db.close()


def init_app(app):
  app.teardown_appcontext(close_db)
  app.cli.add_command(init_db_command)
```
### Register with the Application
```py
# app.py
def create_app(test_config=None):
  ... 
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'gmw.sqlite')
 )
 
  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:y
    pass
    
  db.init_app(app)
  ...

return app
```
### Create Tables
```sql
-- schema.sql
CREATE TABLE box (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  comment TEXT,
  updated_time TEXT NOT NULL,
  created_time TEXT NOT NULL
);

CREATE TABLE goods (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  status TEXT NOT NULL,
  comment TEXT,
  updated_time TEXT NOT NULL,
  created_time TEXT NOT NULL,
  box_id INTEGER NOT NULL,
  FOREIGN KEY (box_id) REFERENCES box(id)
);
```
```py
# db.py
import click

def init_db():
  db = get_db()

  with current_app.open_resource('schema.sql') as f:
    db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
  """Clear the existing data and create new tables."""
  init_db()
  click.echo('Initialized the database.')
```
### Initialize the Database File
```py
# app.py
if __name__ == '__main__':
  app = create_app()
  with app.app_context():
  db.init_db_command()
```
### A Simple Query
```py
# box.py
import json
from db import get_db

@bp.route('/', methods=['GET'])
def get_all_boxes():
  db = get_db()
  response = dict()
  boxes = db.execute(f'SELECT * FROM {TABLE_NAME_BOX}').fetchall()
  for box in boxes:
    response[box[COL_BOX_ID]] = tuple(box[1:])
  return json.dumps(response, ensure_ascii=False)  # ensure_ascii=False: Ensure the correct output of Chinese
```