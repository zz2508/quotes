from flask import Flask 
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
DB_URL='postgresql+psycopg2://zz2508:supersecret@127.0.0.1/quotes'
app.config['SQLALCHEMY_DATABASE_URI']= DB_URL
db = SQLAlchemy(app)

from sqlalchemy import Integer, Text, Boolean
class Quotes(db.Model):
    __tablename__ = 'quotes'
    num = db.Column(Integer, primary_key=True)
    quotes= db.Column(Text) 
    @app.route('/')
    def rand_quote():
        quotes =  Quotes.query.limit(1)
        return render_template('quotes.html',quotes = quotes,)
