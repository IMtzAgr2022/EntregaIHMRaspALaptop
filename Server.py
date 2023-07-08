from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run')
def run_main():
    subprocess.Popen(['python', 'Main.py'])
    return 'Main.py ejecutado'

if __name__ == '__main__':
    app.run()
