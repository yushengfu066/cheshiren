from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database.MysqlData import Loan

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@129.211.167.92:3306/CashManCeShi'

db=SQLAlchemy(app)
r = []
for i in Loan.query.order_by(Loan.id.desc()).limit(1).all():
    res = {}
    res['id'] = i.id
    res['loan_app_id'] = i.loan_app_id
    res['mobile'] = i.mobile
    res['loan_app_status'] = i.loan_app_status
    res['loan_issue_status'] = i.loan_issue_status
    res['status'] = i.status
    r.append(res)
print(r)