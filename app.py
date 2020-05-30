#!/usr/bin/env python
# coding: utf-8
# Date  : 2020/5/30
# Author: zhangyi 
# Email : 450245556@qq.com
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/temp_index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
