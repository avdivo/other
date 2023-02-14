from time import sleep
from pynput import keyboard, mouse


# Действие, когда пользователь нажимает клавишу на клавиатуре
def on_press(key):
    global listen
    if not listen: return
    if key == keyboard.Key.shift_r:
        listen = False # Запретить работать функциям событий
        print('<<< Остановлено прослушивание мыши и клавиатуры')
        return
    print(f'Была нажата клавиша {key}')
    return


# Действие, когда пользователь отпускает клавишу на клавиатуре
def on_release(key):
    if not listen: return
    print(f'Была отпущена клавиша {key}')


# Действие при нажатии кнопки мыши
def on_click(x, y, button, is_pressed):
    if not listen: return
    print(f'Была {"нажата" if is_pressed else "отпущена"} '
          f'клавиша {button} на позиции '
          f'{x} по горизонтали и {y} по вертикали')


# Действие при прокручивании
def on_scroll(x, y, dx, dy):
    if not listen: return
    horizontal_scroll = ''
    if dx < 0:
        horizontal_scroll = 'влево'
    elif dx > 0:
        horizontal_scroll = 'вправо'
    vertical_scroll = ''
    if dy < 0:
        vertical_scroll = 'вниз'
    elif dy > 0:
        vertical_scroll = 'вверх'
    print(f'Была прокрутка '
          f'{horizontal_scroll} {vertical_scroll} на позиции '
          f'{x} по горизонтали и {y} по вертикали')



# Инициализация прослушки клавиатуры
keyboard_listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)

# Прослушка мыши
mouse_listener = mouse.Listener(
    on_click=on_click,
    on_scroll=on_scroll
)



# Старт прослушки мыши
mouse_listener.start()
# Старт прослушки клавиатуры
keyboard_listener.start()
listen = False  # Запретить работать функциям событий

A = True

while A:

    if not listen:

        print("")
        vvedeno_luboe = input("Введите текст: ")
        print("")

        if vvedeno_luboe == ('0'):
            # Стоп прослушки мыши
            mouse_listener.stop()
            # Стоп прослушки клавиатуры
            keyboard_listener.stop()
            A = False

        elif vvedeno_luboe == ('8'):
            listen = True  # Разрешить работать функциям событий
            print('Включено прослушивание мыши и клавиатуры >>>')

    sleep(0.001)

sleep(10)
print('Время закончилось')
