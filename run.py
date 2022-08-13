from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Database environment variables
app.config.update(

    SECRET_KEY='topsecret',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:Hypnosis321T!@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

#Allows Flask to recognes that the DB exists.
db = SQLAlchemy(app)

@app.route('/temp')
def using_template():
    return render_template('hello.html')

@app.route('/watch')
def top_movies():
    movie_list = ['autopsy of jane doe',
                  'neon demon',
                  'ghost in a shell',
                  'kong: skull island',
                  'john wick 2',
                  'spiderman - homecoming']

    return render_template('movies.html',
                           movies=movie_list,
                           name='Harry')

# PUBLICATION TABLE
class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'The id is {}, Name is is {}'.format(self.id, self.name)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


#Old Code
# @app.route('/index')
# @app.route('/')
# def hello_flask():
#     return 'Hello Flask'

#Query String - Normally in key value pair the same as a dictionary. 'greeting' is the key and user creates the value via input url
# @app.route('/new/')
# def query_string(greeting = 'Hello'):
#     query_val = request.args.get('greeting', greeting)
#     return '<h1> the greeting is : {0} </h1>' .format(query_val)

# from flask import Flask, request, render_template
# app = Flask(__name__)
# def hello_flask():
#
# @app.route('/index')
# @app.route('/')
# def hello_flask():