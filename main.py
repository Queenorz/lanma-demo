import datetime

from flask import Flask,render_template


app = Flask(__name__,static_url_path='/')

@app.route('/txmaaa')
def hello():

    return render_template('1.html')

@app.route('/jilu/<name>')
def jilu(name):
    t = datetime.date.today()
    m = t.month
    d = t.day
    print(m,d)
    return render_template('2.html',name=name,month=m,day=d)

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=8877,debug=True)
