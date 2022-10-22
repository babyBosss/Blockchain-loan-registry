from flask import Flask, render_template, redirect, url_for, request
from block import *

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        lender = request.form['lender']
        amount = request.form['amount']
        receiver = request.form['receiver']
        write_block(name=lender, amount=amount, receiver=receiver)
        return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/cheking', methods=['GET'])
def check():
    results = check_integrity()
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
