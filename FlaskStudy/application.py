import datetime
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html")

@app.route('/more')
def more():

    return render_template("more.html")



# @app.route('/bye')
# def bye():
#     headline="goodbye "
#     return render_template("index.html",head=headline)

#
# @app.route('/newyear')
# def newyear():
#     now=datetime.datetime.now()
#     headline= now.month==1 and now.day==1
#
#     return render_template("index.html",head=headline)
# @app.route('/names')
# def names():
#     name=["nidhish","niharika","chand"]
#     return render_template("index.html",names=name)
#
# @app.route('/nidhish')
# def nidhish():
#     return 'Hello, Nidhish!'

# #routing to any name
# @app.route('/<string:anyname>')
# def hello(anyname):
#     anyname=anyname.capitalize()
#     return f'<h1>Hello, {anyname}!</h1>'
if __name__=='__main__':
    app.run(debug=True)
    app.debug(host="0.0.0.0",port=5000)