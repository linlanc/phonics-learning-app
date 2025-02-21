from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/voice2')
def voice2():
    return render_template('voice2.html')

@app.route('/static/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('static/audio', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=52437)
