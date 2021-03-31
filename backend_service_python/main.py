#!/usr/bin/env python
# -*- conding: utf-8 -*-
# @Author:xxx
# @Time : 2021/3/27 12:50
# @File :main.py
# @Software:
from database import app,api
from Backend.login import Login,LoanCashman,payCashman
from flask_cors import CORS
from Backend.logs import logger
CORS(app)

logger.info(app)
logger.debug(app)
logger.error(app)
api.add_resource(Login,'/login')
api.add_resource(LoanCashman,'/loan')
api.add_resource(payCashman,'/repayment')
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )



