from flask import Flask

app =Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/about')
def about():
    return '<h1>About Page</h1>'   


if(__name__=='__main__'):
    app.run(debug=True)

