from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola Jairo, en qué puedo ayudarte?.'

if __name__ == '__main__':
    app.run()