'''
导入模块
'''

'''
1.pip install flask
2.from flask import Flask

'''
from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def index():
    return "首页"

@app.route("/wzk")
def wzkinfo():
    return "王增柯的主页"

@app.route("/wzk/pay")
def wzkpay():
     return render_template('pay.html',name="zzy")

app.run()
