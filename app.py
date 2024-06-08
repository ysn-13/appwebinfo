from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/web_dev')
def web_dev():
    return render_template('web_dev.html')

@app.route('/networks')
def networks():
    return render_template('networks.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')

@app.route('/cybersecurity')
def cybersecurity():
    return render_template('cybersecurity.html')

if __name__ == '__main__':
    app.run(debug=True)
