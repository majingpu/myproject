#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from flask_script import Manager
from demo import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()