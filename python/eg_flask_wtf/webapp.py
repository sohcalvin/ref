from flask_wtf import Form
from wtforms import StringField


from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = 'development key'


class ContactForm(Form):
   name = StringField("Name Of Student")


@app.route('/contact')
def contact():
   form = ContactForm()
   return render_template('./contact.html', form = form)

if __name__ == '__main__':
   app.run(debug = True)