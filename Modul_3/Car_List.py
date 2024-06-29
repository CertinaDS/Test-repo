import pandas as pd
from PIL import Image
import random
from IPython.display import HTML

var = ['предпочитает', 'не любит', 'любит', 'обожает', 'никогда не ездил на', 'хочет прокатиться на']

color = {
    'черный': 'черном',
    'синий': 'синем',
    'серый': 'сером',
    'красный': 'красном',
    'зеленый': 'зеленом',
    'голубой': 'голубом',
    'бирюзовый': 'бирюзовом',
    'розовый': 'розовом',
    'белый': 'белом',
    'оранжевый': 'оранжевом',
    'малиновый': 'малиновомом',
    'бежевый': 'бежевом',
    'золотой': 'золотом',
    'желтый': 'желтом'
}

drivers = {
    'Зуйков Анатолий': r'C:\Users\User\Desktop\Фото\Зуйков Анатолий.jpg',
    'Исаев Александр': r'C:\Users\User\Desktop\Фото\Исаев Александр.jpg',
    'Кашубин Александр': r'C:\Users\User\Desktop\Фото\Кашубин Александр.jpg',
    'Кузин Виктор': r'C:\Users\User\Desktop\Фото\Кузин Виктор.jpg',
    'Ломазов Евгений': r'C:\Users\User\Desktop\Фото\Ломазов Евгений.jpg',
    'Матвеенко Дмитрий': r'C:\Users\User\Desktop\Фото\Матвеенко Дмитрий.jpg',
    'Можаев Илья': r'C:\Users\User\Desktop\Фото\Можаев Илья.jpg',
    'Первинкин Константин': r'C:\Users\User\Desktop\Фото\Первинкин Константин.jpg',
    'Собольков Дмитрий': r'C:\Users\User\Desktop\Фото\Собольков Дмитрий.jpg',
    'Суменко Константин': r'C:\Users\User\Desktop\Фото\Суменко Константин.jpg',
    'Шаров Артем': r'C:\Users\User\Desktop\Фото\Шаров Артем.jpg',
    'Гоцеридзе Шота': r'C:\Users\User\Desktop\Фото\Гоцеридзе Шота.jpg',
    'Зуйков Анатолий': r'C:\Users\User\Desktop\Фото\Зуйков Анатолий.jpg',
    'Рудавина Юля': r'C:\Users\User\Desktop\Фото\Юля.jpg'
}

cars = {
    'Infinity': r'C:\Users\User\Desktop\AUTO\infinity.jpeg',
    'Toyota': r'C:\Users\User\Desktop\AUTO\toyota.jpeg',
    'Ford': r'C:\Users\User\Desktop\AUTO\ford.jpeg',
    'Honda': r'C:\Users\User\Desktop\AUTO\honda.jpeg',
    'Hyundai': r'C:\Users\User\Desktop\AUTO\hyundai.jpeg',
    'Mercedes': r'C:\Users\User\Desktop\AUTO\mercedes.jpg',
    'Geely': r'C:\Users\User\Desktop\AUTO\geely.jpeg',
    'KIA': r'C:\Users\User\Desktop\AUTO\kia.jpeg',
    'Nissan': r'C:\Users\User\Desktop\AUTO\nissan.jpeg',
    'Chevrolet': r'C:\Users\User\Desktop\AUTO\chevrolet.jpeg',
    'Volvo': r'C:\Users\User\Desktop\AUTO\volvo.jpeg',
    'Rolls Royce': r'C:\Users\User\Desktop\AUTO\rolls_royce.jpeg',
    'BMW': r'C:\Users\User\Desktop\AUTO\bmw.jpg',
    'Mustang': r'C:\Users\User\Desktop\AUTO\Mustang.jpg'
}

col_ = list(color.keys())
cars_ = list(cars.keys())
drivers_ = list(drivers.keys())
df = pd.DataFrame()
for i in range(len(drivers)):
    d = random.choice(drivers_)
    c = random.choice(cars_)
    F = drivers.get(d)
    v = random.choice(var)
    col = random.choice(col_)
    url = cars.get(c)
    synt = color.get(col)
    s1 = v[-2:]    
    if s1 in ('ет','ит'):
        if url != '':
            img = Image.open(url)
            df = df.append({'ФОТО' : f"{F}", 'Имя' : f"{d} {v}", 'Цвет' : f"{col}", 'Автомобиль' : f"{c} " , 'Фото' : f"{url}"}, ignore_index = True)
            cars_.remove(c)
            drivers_.remove(d)
            col_.remove(col)
    elif s1 in ('ил', 'на'):
        if url != '':
            img = Image.open(url)
            df = df.append({'ФОТО' : f"{F}", 'Имя' : f"{d} {v}", 'Цвет' : f"{synt}", 'Автомобиль' : f"{c}" , 'Фото' :  f"{url}"}, ignore_index = True)
            cars_.remove(c)
            drivers_.remove(d)
            col_.remove(col)
pd.set_option('display.max_colwidth', -1)


def to_FOTO_tag(path): return '<img src="'+ path + '"width="400" >'
def to_foto_tag(path): return '<img src="'+ path + '"width="700" >'
display(HTML(df.to_html(escape=False,formatters=dict(Фото=to_foto_tag, ФОТО=to_FOTO_tag))))