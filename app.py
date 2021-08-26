from flask import Flask, render_template, request
from flask_mail import Mail, Message
import config
from searching import search
import os

app = Flask(__name__)
# mailing
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='graymatter626@gmail.com',
    MAIL_PASSWORD='Graymatter626!',
)
mail = Mail(app)


@app.route('/')
@app.route("/index/")
def index():
    return render_template('index.html', success=False, error=False)


# mailingfeature
@app.route("/send_email/", methods=['POST'])
def send_email():
    if request.method == 'POST':
        keyword = request.form['keyword']
        imageNumber = int(request.form['imageNumber'])
        print(type(imageNumber))
    if keyword == '' or imageNumber == '':
        return render_template('index.html', message='Please enter required fields')
    search(keyword, imageNumber)

    msg = Message("Images sent from {} using Piccauto".format(request.form['name']),
                  sender='graymatter626@gmail.com',
                  body="",
                  recipients=[request.form['email']])
    with app.open_resource('images.zip') as fp:
        msg.attach('images.zip', "application/zip", fp.read())
    mail.send(msg)

    os.remove("./images.zip")
    return render_template('success.html')


if __name__ == "__main__":

    # send_email()
    app.run(debug=True)
