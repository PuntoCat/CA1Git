from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Flask'

#Query String - Normally in key value pair the same as a dictionary. 'greeting' is the key and user creates the value via input url
@app.route('/new/')
def query_string(greeting = 'Hello'):
    query_val = request.args.get('greeting', greeting)
    return '<h1> the greeting is : {0} </h1>' .format(query_val)

if __name__ == '__main__':
    app.run(debug=True)


#Old Code
# from flask import Flask, request, render_template
# app = Flask(__name__)
# def hello_flask():
#
# @app.route('/index')
# @app.route('/')
# def hello_flask():