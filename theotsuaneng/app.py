from flask import Flask
 
app = Flask(__name__)
 
@app.route('/hello')
def hello():
    return 'Hello World'
 
app.run(host='0.0.0.0', port=5000) 

app.py
#URL: http://localhost:5000/hello