import os
from flask import Flask
from routes import BLUEPRINT

app = Flask(__name__)
app.register_blueprint(BLUEPRINT)


if __name__ == '__main__':
    app.run(debug=True, host=os.getenv('HOST', 'localhost'), port=os.getenv('PORT', 5000))
