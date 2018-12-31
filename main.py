from flask import Flask, request, render_template
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route('/')
@app.route('/home')
def home():
  user_agent = request.headers.get('User-Agent')
  return render_template('home.html', useragent=user_agent)


@app.route('/documentation')
def documentation():
  return render_template('documentation.html')


@manager.command
def hello():
  print("Hello, world!")

@app.route('/user/<name>')
def user(name):
  return render_template('user.html', name=name)


if __name__ == '__main__':
  manager.run()