import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

board = requests.get('http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(board.text, 'html.parser')

courses = [str(i).strip().replace('<table class="mfd-table mfd-currency-table">','')\
               .replace('<tr>','')\
               .replace('<th class="mfdSortDESC">','')\
               .replace('</th>','')\
               .replace('<th>','')\
               .replace('<td>','')\
               .replace('</td>','')\
               .replace('<span class="mfd-u">','')\
               .replace('</span>','')\
               .replace('<span class="mfd-d">','')\
               .replace('[','')\
           for i in str(soup.find_all(class_="mfd-table mfd-currency-table")).split("</tr>")]
courses = [i.strip().split('\n') for i in courses[0:-1]]

df = pd.DataFrame(courses)
df = df.drop([0,1])
df.columns = ['Дата', 'Курс', 'Изменение']
print(df.to_markdown(tablefmt="grid", stralign='center'))

df['Курс'] = df['Курс'].astype(float)

X_data = df['Дата'].tolist()
Y_rate = df['Курс'].tolist()

plt.figure(figsize=(20,12))
plt.xlabel('Дата')
plt.ylabel('Курс')
plt.plot(X_data, Y_rate, 'r')
plt.title('Курс доллара')
plt.xticks(rotation=90)
plt.gca().invert_xaxis()
plt.show()
