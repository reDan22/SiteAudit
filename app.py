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

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        # Обработка POST-запроса (например, формы обратной связи)
        user_name = request.form.get('name')
        user_message = request.form.get('message')
        return f"Приняли сообщение от {user_name}: {user_message}"
    else:
        # При GET-запросе — показываем форму contacts.html
        return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)
