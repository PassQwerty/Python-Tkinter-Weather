from tkinter import *
from tkinter import messagebox
import requests


# API-ключ для доступа к сервису погоды
apiKey = 'e9a5d3b74bf84418b11193028231901'


def get_weather_data(passInput, city):
    # формирование URL-адреса для запроса погоды
    url = f"http://api.weatherapi.com/v1/current.json?key={apiKey}&q={city}"
    # отправка GET-запроса на получение погоды
    response = requests.get(url)
    # получение ответа в формате JSON и сохранение данных в переменную
    data = response.json()

    # получение названия города из данных погоды
    name = data['location']['name']
    # получение названия страны из данных погоды
    country = data['location']['country']
    # получение текущей температуры в градусах Цельсия из данных погоды
    current_temp_c = data['current']['temp_c']
    # получение текущей погоды (например, "облачно") из данных погоды
    current_mist = data['current']['condition']['text']

    # форматирование строки для отображения информации о погоде
    formatReq = f"Информация о погоде\
        \n\nСтрана: {country}\
        \nГород: {name}\
        \nТек. температура °C: {current_temp_c}\
        \nТекущая погода: {current_mist}"

    # отображение диалогового окна с информацией о погоде
    messagebox.showinfo(title='Название', message=formatReq)

    passInput.delete(0, END)


def main():
    # создание главного окна
    root = Tk()

    # установка цвета фона главного окна
    root['bg'] = '#fff'
    # установка заголовка главного окна
    root.title('Погода')
    # установка размеров и позиции главного окна
    root.geometry('300x250+850+400')
    # запрет на изменение размера главного окна
    root.resizable(width=False, height=False)

    # создание метки с текстом "Введите название города"
    title = Label(root, text="Введите название города", bg='white', font=40)
    # установка метки на главном окне с отступом сверху и снизу
    title.pack(pady=10)

    # создание поля ввода для ввода названия города
    passInput = Entry(root, bg='white', width=20, justify='center', font=20)
    # установка поля ввода на главном окне
    passInput.pack()

    # создание кнопки "Узнать погоду" с вызовом функции get_weather_data при нажатии на кнопку
    btn = Button(root, text='Узнать погоду', bg='red', height=1, width=15, font=20, fg='#fff',
                 command=lambda: get_weather_data(passInput, passInput.get()))
    # установка кнопки на главном окне с отступом сверху
    btn.pack(pady=(10, 0))

    # запуск цикла обработки событий главного окна
    root.mainloop()


# проверка, является ли данный файл главным модулем программы
if __name__ == "__main__":
    # вызов функции main(), если файл является главным модулем
    main()
