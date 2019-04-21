from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html', title='Gallery')

@app.route("/codes")
def codes():
    return render_template('codes.html', title='Codes')

if __name__ == '__main__':
    app.run(debug=True)
