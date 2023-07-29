import random
import pyjokes


def show_menu():
    print(''' Меню:
        1. Порекомендувати фільм
        2. Порекомендувати музику
        3. Гра "Камінь, ножиці, папір"
        4. Порекомендувати анекдоти
        5. Порекомендувати цікаві факти про Python
        6. Вихід''')


def recommend_film():
    films = ["Оппенгеймер", "Залізна людина",
             "Топ Ґан: Меверік", "Месники", "Вартові галактики"]
    film = random.choice(films)
    print(f"Рекомендую подивитись цей фільм: {film}")


def recommend_music():
    songs = ["Summer", "Starboy", "The Hills",
             "Ain't No Mountain High Enough", "Chlorine"]
    song = random.choice(songs)
    print(f"Рекомендую послухати цю пісню: {song}")


def game():
    print("Введіть камінь, ножиці чи папір")
    choices = ["камінь", "ножиці", "папір"]
    user_choice = input("Ви: ")
    random_choice = random.choice(choices)
    print("Бот: ", random_choice)

    if user_choice == random_choice:
        print("Нічія")
        game()
    elif (user_choice == "камінь" and random_choice == "ножиці") or (user_choice == "ножиці" and random_choice == "папір") or\
         (user_choice == "папір" and random_choice == "камінь"):
        print("Ви виграли!")
    else:
        print("Ви програли")


def recommend_joke():
    print(pyjokes.get_joke())


def recommend_facts():
    facts = [
        "Створення та перший реліз: Python був створений Гвідо ван Россумом і вперше випущений у 1991 році. Походження назви мови пов'язано з захопленням творця мови телевізійною програмою \"Монті Пайтоновський літак\"",
        "Інтерпретована мова: Python є інтерпретованою мовою програмування, що означає, що програми можуть виконуватись без попередньої компіляції. Це робить його дуже доступним та зручним для швидкої розробки.",
        "Простота та читабельність: Однією з головних філософій Python є \"читабельність коду\", що робить його приємним для розробників та підвищує продуктивність. Python став відомий своїми чіткими та зрозумілими синтаксисом, який нагадує англійську мову.",
        "Багатий екосистема: Python має широку та активну спільноту, яка створює багато корисних пакетів і бібліотек. PyPI (Python Package Index) містить понад сотні тисяч пакетів, які допомагають розробникам вирішувати різноманітні задачі.",
        "Універсальність: Python є універсальною мовою, що підходить для різноманітних завдань. Він використовується в веб-розробці (наприклад, Django та Flask), наукових дослідженнях (завдяки бібліотекам NumPy, SciPy та Pandas), штучному інтелекті (за допомогою TensorFlow та PyTorch), а також для розробки десктопних програм і скриптів."]
    fact = random.choice(facts)
    print(f"Цікавий факт: {fact}")


def main():
    while True:
        show_menu()
        operation = input("Виберіть операцію: ")

        if operation == '1':
            recommend_film()
        elif operation == '2':
            recommend_music()
        elif operation == '3':
            game()
        elif operation == '4':
            recommend_joke()
        elif operation == '5':
            recommend_facts()
        elif operation == '6':
            print("Ви вийшли з програми")
            break
        else:
            print("Немає такого в меню, спробуйте ще раз")


if __name__ == '__main__':
    main()
