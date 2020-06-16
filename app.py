from idea import app, mail
from flask import render_template, session, request, redirect, url_for, flash, abort
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nextPage')
def nextPage():
    return render_template('nextPage.html')

   

if __name__ == '__main__':
    app.run(debug=False)
