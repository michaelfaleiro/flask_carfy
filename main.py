from flask import Flask
from auth.auth import auth_blueprint
from home.home import home_blueprint


app = Flask(__name__)
app.register_blueprint(auth_blueprint)
app.register_blueprint(home_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
