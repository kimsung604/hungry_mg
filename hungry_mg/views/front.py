# coding: utf-8

from flask import Blueprint, render_template

app = Blueprint('front', __name__)


@app.route('/')
def welcome():
    return render_template('index.html')
