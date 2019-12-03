from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page! TESTE1'


if __name__ == '__main__':

    app.run()
