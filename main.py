from flask import Flask, render_template

app = Flask(__name__)

@app.route('/tweet')
def tweet():
    return render_template('tweet.html')

@app.route('/send-tweet')
def send_tweet():
    return 'Ok!'

if __name__ == '__main__':
    app.run(debug=True)
