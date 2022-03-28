from flask import Flask, render_template

#creating a flask instance
app = Flask(__name__)

#creating a route/decorator to home page
@app.route('/')
def home():
    pizza = ['margherita', 'pepperoni', 'deluxe', 'meat tornado', 'vegetarian']
    return render_template('home.html',
        pizza = pizza
        )

#routing to users
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', 
        user_name = name
        )

#invalid url handling
@app.errorhandler(404)
def pagenotfount(e):
    return render_template('404.html'), 404

#server error handling
@app.errorhandler(500)
def pagenotfount(e):
    return render_template('500.html'), 500