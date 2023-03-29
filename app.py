from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''Hello, World! testing test
    <h1> just adding some more text</h1>
    <h2> adding more text </h2>
    <a href='/otherpage'> Got to otherpage </a>
    '''

@app.route('/otherpage')
def otherindex():
    return '''THis is a differnt page
    <h1> just adding some more text</h1>
    <h2> adding more text </h2>
    <a href='/'> home </a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
