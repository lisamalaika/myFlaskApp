from flask import Flask, render_template
from data import Articles
from generatestrain import generate_strain

Articles = Articles()
generator = generate_strain()

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=["POST", "GET"])
def home():
    return render_template('home.html')
    name = generator.name()
    response = {"name": name}

    return jsonify(response)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)

