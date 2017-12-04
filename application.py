from flask import Flask, flash, redirect, render_template, request, url_for
from flask_mail import Mail, Message
from tempfile import mkdtemp
import sys, os
from derange import *
from checkfordupes import *

# configure application
app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ['GMAIL_ADDRESS']  # you need to provide this
app.config['MAIL_PASSWORD'] = os.environ['GMAIL_PASSWORD']  # you need to provide this
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

# the app itself
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        #extract data from front-end forms
        names = request.form.getlist('name')
        emails = request.form.getlist('email')
        radio = request.form['wannaSeeResults']
        l = []

        #store names and emails in list
        for i in range(len(names)):
           l.append((names[i], emails[i]))

        #check for duplicates if front-end validation failed for some reason
        if checkForDupes(l):
            return render_template("invalid.html")

        #derange list
        l2=derange(l)

        #send emails to gifters and giftees
        for i in range(len(names)):
            msg = Message('Secret Santa', sender = 'Secret Santa', recipients = [l[i][1]])
            msg.body = """
Hi {},

Your Secret Santa giftee is {}. Time to get down to shopping! :)

Yours,
Santa
            """.format(l[i][0], l2[i][0])
            try:
                mail.send(msg)
            except:
                return render_template("wrong.html")

        #send results email
        if radio=='yes':
            msg = Message('Secret Santa', sender = 'Secret Santa', recipients = [l[0][1]])
            msg.html = """
            </head>
            <body>
            <p>Hi,</p><p>The Secret Santa results are the following:</p>
            <table  style="padding: 5px; margin: 5px">
            <tr><th>Person</th><th>Giftee</th></tr>"""

            for i in range(len(names)): 
                msg.html += """
                <tr><td>{}</td><td>{}</td></tr>
                """.format(l[i][0], l2[i][0])
            
            msg.html += """
            </table><p>Best,</p><p>Santa</p></body></html>
            """
            try:
                mail.send(msg)
            except:
                return render_template("wrong.html")


        return render_template("emails-sent.html")

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8000)