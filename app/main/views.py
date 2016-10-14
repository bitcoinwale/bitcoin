from flask import render_template, session, redirect, url_for, request
from ..main import main
import json
from .forms import MainForm
from ..models import User
from app import db
import time


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/buybitcoin')
def buybitcoin():
    return render_template('buybitcoin.html')


@main.route('/purchaseid')
def purchaseid():
    return render_template('purchaseid.html')


@main.route('/purchase/form')
def purchase_form():
    form = MainForm()
    return render_template('sign_up_form.html', form=form)


@main.route('/contactus')
def contactus():
    return render_template('contactus.html')


@main.route('/query/form')
def contact_form():
    return render_template('')


@main.route('/howitwork')
def howitwork():
    return render_template('howitwork.html')


@main.route('/bitcoin-mining-india')
def bitcoin_mining_india():
    return render_template('bitcoin-mining-india.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/bitcoingraph')
def bitcoingraph():
    return render_template('bitcoingraph.html')


@main.route('/terms')
def terms():
    return render_template('terms.html')


@main.route('/faq')
def faq():
    return render_template('faq.html')


@main.route('/bitcointwallet')
def bitcoinwallet():
    return render_template('bitcoinwallet.html')


@main.route('/bitinvest')
def bitinvest():
    return render_template('bitinvest.html')


@main.route('/bitcoinhalving')
def bitcoinhalving():
    return render_template('bitcoinhalving.html')


@main.route('/helpingguide1')
def helpingguide1():
    return render_template('helpingguide1.html')


@main.route('/notfound')
def notfound():
    return render_template('404.html')


@main.route('/base', methods=['GET', 'POST'])
def base():
    form = MainForm()
    if request.method == 'GET':
        return render_template('extends.html', form=form)
    if request.method == 'POST':
        print(form.errors)
        if form.is_submitted():
            print("submitted")
        if form.validate():
            print('validated')
            u = User()
            u.name = form.name.data
            u.email_id = form.email.data
            u.mob_no = form.number.data
            u.password = form.password.data
            u.complete_registration = False
            u.gender = form.gender.data
            u.pincode = form.pincode.data
            u.timestamp = time.time()
            db.session.add(u)
            #db.session.commit()
            u = User.query.all()
            return render_template('extends2.html', u=u)
        else:
            print('something is wrong')


def bitcoin_value():
    url = "http://api.coindesk.com/v1/bpi/currentprice.json"
    json.loads(url)