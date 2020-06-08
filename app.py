from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_cors import CORS, cross_origin
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text, func
from datetime import datetime
import time
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///us-census.db'
db = SQLAlchemy(app)

Base = declarative_base()

class DataList(Base):
    __tablename__ = 'census_learn_sql'
    idx = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    class_of_worker = db.Column(db.String(1000))
    industry_code = db.Column(db.String(1000))
    occupation_code = db.Column(db.String(1000))
    education = db.Column(db.String(1000))
    wage_per_hour = db.Column(db.String(1000))
    last_education = db.Column(db.String(1000))
    marital_status = db.Column(db.String(1000))
    major_industry_code = db.Column(db.String(1000))
    mace = db.Column(db.String(1000))
    hispanice = db.Column(db.String(1000))
    sex = db.Column(db.String(1000))
    member_of_labor = db.Column(db.String(1000))
    reason_for_unemployment = db.Column(db.String(1000))
    fulltime = db.Column(db.String(1000))
    capital_gain = db.Column(db.String(1000))
    capital_loss = db.Column(db.String(1000))
    dividends = db.Column(db.String(1000))
    income_tax_liability = db.Column(db.String(1000))
    previous_residence_region = db.Column(db.String(1000))
    previous_residence_state = db.Column(db.String(1000))
    household_with_family = db.Column(db.String(1000))
    household_simple = db.Column(db.String(1000))
    weight = db.Column(db.String(1000))
    msa_change = db.Column(db.String(1000))
    reg_change = db.Column(db.String(1000))
    within_reg_change = db.Column(db.String(1000))
    lived_here = db.Column(db.String(1000))
    migration_prev_res_in_sunbelt = db.Column(db.String(1000))
    num_persons_worked_for_employer = db.Column(db.String(1000))
    family_members_under_118 = db.Column(db.String(1000))
    father_birth_country = db.Column(db.String(1000))
    mother_birth_country = db.Column(db.String(1000))
    birth_country = db.Column(db.String(1000))
    citizenship = db.Column(db.String(1000))
    own_business_or_self_employed = db.Column(db.String(1000))
    fill_questionnaire_for_veteran_admin = db.Column(db.String(1000))
    veretans_benefits = db.Column(db.String(1000))
    weeks_worked_in_year = db.Column(db.String(1000))
    year = db.Column(db.String(1000))
    salary_range = db.Column(db.String(1000))

    def __repr__(self):
        return '<DataList %r>' % self.age



@app.route('/time')
def hello_world():
    return {'time': time.time()}

@cross_origin()
@app.route('/census/<string:field>')
def get_fields_name(field):

    print(field)
    data = []
    fields = db.session.query(getattr(DataList, field), func.avg(DataList.age), func.count()).filter(DataList.age.isnot(None)).group_by(getattr(DataList, field)).order_by(func.count().desc()).limit(100).all()
    for field in fields:
        data.append(field)

    return jsonify(
            {"status": "success",
            "data" : data}
            )

if __name__ == '__main__':
    app.run()
