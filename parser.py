from tkinter import *
import requests

class Func:
    """Класс отвечает за работу приложения"""
    def __init__(self, rut): # __init__ предназаначен для облегчения работы с кодом
        """Расположение элементов в окне приложения"""
        self.rut=rut
        self.rut.resizable(height=False,width=False)# нельзя изменять размеры окна приложения
        self.rut.geometry('400x400')# установление размеров приложения
        self.rut.title('Parser')# название программы
        self.rut['bg']='#c2b8b8'# цвет окна приложения
        self.rut.iconphoto(True, PhotoImage(file='icon.png'))# предназначена для установления значка приложения
        self.pole=StringVar()# переменная со значением из поля ввода
        self.pole1=Entry(root, font=('Meiryo', 10), bg='#84c2a8', textvariable=self.pole, justify='center')# поле ввода
        self.pole1.place(x=125,y=100)#расположение поля ввода
        self.metka=Label(root, text='Парсер криптовалюты', bg='#50f2e7', font=('FangSong', 15, 'bold'), justify='center') # метка / заголовок с названием приложения
        self.metka.place(x=2.2,y=5)# расположение метки / заголовка с названием приложения
        self.knopka=Button(root, text='Начать парсинг!', bg='#05ad9a', fg='#1c1b17',command=self.crypto) # Кнопка запуска парсинга
        self.knopka.place(x=123,y=200)# расположение кнопки
        self.knopka1=Button(root,text='Очистка', bg='#05ad9a', fg='#1c1b17',command=self.dellab) # Кнопка очитски меток
        self.knopka1.place(x=232,y=200)# расположение кнопки очистки
    def crypto(self):
        """ФУНКЦИЯ ПРЕДНАЗНАЧЕНА ДЛЯ ПАРСИНГА КРИПТОВАЛЮТЫ С САЙТА COINMARKETCAP"""
        self.request=requests.get(url='https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=10000').json()
        for i in self.request['data']['cryptoCurrencyList']:# перебор словаря с информацией о криптовалюте
            if i.get('name') == self.pole.get(): # Проверка и сравнение значения из поля ввода и названия криптовалюты
                self.nazvanie=i['name']# переменная с названием криптовалюты
                self.tsena=i['quotes'][0]['price']# переменная с ценой
                self.rezultat=f'Название: {self.nazvanie}\nЦена: {self.tsena:.2f}$'# переменная с названием и ценой криптовалюты
                self.lab=Label(root, text=self.rezultat, justify='center', bg='#f5d256', font=('Sitka Heading', 15,'bold')) # Создание метки с названием и ценой криптовалюты
                self.lab.place(x=125,y=300)# расположение метки с названием и ценой криптовалюты
        # if crypto() == False:
        #     lab.destroy()
    def dellab(self):
        """Функция для кнопки удаления метки"""
        """На кнопку очистки нажимать после каждого раза парсинга!!!!"""
        self.lab.destroy()


if __name__ == '__main__': # типо работает как защитник
    root=Tk()# создание окна
    okno=Func(root)# класс с аргументом значений из окна
    root.mainloop()# завершение программы