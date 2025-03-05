from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    # Показываем шаблон index.html — главную страницу
    return render_template('welcome.html')

@app.route('/about')
def about():
    # Показываем шаблон about.html
    return render_template('about.html')

@app.route('/audit')
def audit():
    # Показываем шаблон about.html
    return render_template('audit.html')

if __name__ == "__main__":
    app.run(debug=True)
