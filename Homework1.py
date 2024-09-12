from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def date_and_time():
    # Получаем текущие дату и время
    now = datetime.datetime.now()
    # Форматируем дату и время в строку
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # Передаем переменную в шаблон
    return render_template('hw1.html', time=formatted_time)

if __name__ == "__main__":
    app.run()