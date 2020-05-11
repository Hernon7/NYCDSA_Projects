from flask import Flask, render_template, json, request, Markup

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/aboutus')
def signUp():

    return render_template('aboutus.html')


if __name__ == '__main__':
    app.run(threaded=True)
