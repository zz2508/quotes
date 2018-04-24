from flask import Flask 
from flask import render_template
from random import randrange
app = Flask(__name__)

@app.route('/')
def rand_quote():
    with open('inspiration.txt') as fp:
        
        quote = fp.read().split('\n')
    k = randrange(0,len(quote))
    quotes =quote[k]
    return render_template('quotes.html',quotes = quotes)
