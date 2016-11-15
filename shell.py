from flask import Flask, request, redirect, url_for, render_template, flash

from shell_app import auth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qweradfvartaeefvadfgtadfvcbsrt'
app.register_blueprint(auth)


@app.context_processor
def include_template_variables():
    return {'permission': 'adf'}


@app.route('/')
def index():
    print(request.endpoint)
    flash('something is wrong')
    return render_template('base1.html')


@app.route('/hello')
def hello():
    print(request.endpoint)
    return redirect(url_for('index'))

app.debug = True
app.run()
