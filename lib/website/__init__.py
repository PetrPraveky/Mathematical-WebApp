from flask import Flask, Blueprint, render_template, url_for, redirect
import os

def views_site():
    views = Blueprint(
        'views',
        __name__,
        static_folder='static',
        template_folder='../../src/templates'
    )
    
    @views.route('/')
    def index():
        return redirect(url_for('views.home'))
    @views.route('/home')
    def home():
        return render_template('home.html')
    
    return views

def create_app():
    with open(os.path.join('lib', 'key.0'), "r", encoding="utf-8") as k:
        key = k.read()
        k.close()
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = key
    
    app.register_blueprint(views_site(), url_prefix="/")
    
    return app