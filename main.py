import numpy as n
from PIL import Image
import requests
from rich.console import Console

print(20 * '=', 'NUMPY', 20 * '=')

num = n.array([1, 2, 3, 4, 5])
print(num)
num = n.array([1, 2, 3, 4, 5], 'float32')  # --> Преобразования объекта в число с плавающей точкой
print(num)
num = n.array([1, 2, 3, 4, 5], 'str_')  # --> Преобразования объекта в строку
print(num)
num = n.int32(3.5)  # --> Получения целого числа
print(num)
num = n.mean([1, 2, 3, 4, 5])  # --> Среднее значение
print(num)
num = n.sqrt(16) # --> Квадратный корень
print(num)


print(20 * '=', 'PILLOW', 20 * '=')

im = Image.open('images/'+'fon.jpeg')
# im.show()
print(im.size)
print(im.format)
edit = im.crop((0, 0, im.width, im.width)).resize((500, 250)).transpose(Image.FLIP_TOP_BOTTOM)
#edit.show()

print(20 * '=', 'REQUESTS', 20 * '=')

resp = requests.get('https://google.com')
print(resp.status_code)
print(resp.text)

resp = requests.get('https://api.github.com')
print(resp)
print(resp.headers) # --> Для получения заголовки ответа
print(resp.request.headers)  # --> Для получения заголовки запроса

print(20 * '=', 'RICH', 20 * '=')
# Библиотека для форматирования вывода на экран простых и сложных структур.
cons = Console()
cons.print('[red]Hello[/red] [blue]world[/blue]')
cons.print('Hello', style='red')
cons.print('Hello', justify='center')


# Благодаря библиотекам, разработчику не приходится писать все с нуля,
# так как в них реализован весь функционал решения