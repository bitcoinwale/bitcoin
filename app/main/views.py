from flask import render_template, session, redirect, url_for, request, flash
from ..main import main
import json
from .forms import QueryForm
from ..auth.forms import RegistrationForm
from ..models import User, Contact, Values
from app import db
from datetime import datetime
from urllib.request import urlopen


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
    form = RegistrationForm()
    return render_template('sign_up_form.html', form=form)


@main.route('/contactus')
def contactus():
    return render_template('contactus.html')


@main.route('/query/form', methods=['GET', 'POST'])
def contact_form():
    form = QueryForm()
    if request.method == 'GET':
        return render_template('query_form.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            c = Contact()
            c.email = form.email.data
            c.mob = form.number.data
            c.name = form.name.data
            c.ques = form.query.data
            c.description = form.description.data
            c.timestamp = datetime.now()
            db.session.add(c)
            db.session.commit()
            return redirect(url_for('main.thank', type='1', id=c.id))
        else:
            print(form.errors)
            for i in form.errors:
                flash(i)
            return redirect(url_for('main.contact_form'))


@main.route('/thankyou')
def thank():
    type = request.args.get('type')
    if type == '1':
        user = Contact.query.get(request.args.get('id'))
        print(user.name)
        return render_template('thank.html', id=user)
    return render_template('thank.html')


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
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('base1.html')
    if request.method == 'POST':
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
            u.timestamp = datetime.now()
            db.session.add(u)
            db.session.commit()
            u = User.query.all()
            return render_template('extends2.html', u=u)
        else:
            print(form.errors)
            for i in form.errors:
                flash(i)


@main.context_processor         # to add variables in template scope
def include_template_variables():
    return {'Permission': 'adf'}
    pass


@main.route('/api')
def bitcoin_value():
    url = "http://api.coindesk.com/v1/bpi/currentprice.json"
    url = urlopen(url)
    url = url.read().decode("utf-8")
    data = json.loads(url)
    return data


@main.route('/api/current.json')
def api():
    latest = Values.query.all()[-1]

    values = {'time': str(latest.timestamp) + ' UTC+05:30',
              'rates': {'bid': latest.bid, 'ask': latest.ask}}
    return json.dumps(values)
