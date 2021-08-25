#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from flask import Flask, jsonify

# init app
app = Flask (__name__)
# env config
app.config.from_object('config.DevelopmentConfig')


@app.route ('/ping_pong', methods=['GET'])
def ping_pong():
    return jsonify ({
        'status': 'success',
        'message': 'pong'
    })
