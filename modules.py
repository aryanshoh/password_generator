digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'


def get_passwords_count():
    while True:
        how_many_passwords = input('Сколько паролей Вы хотите сгенерировать? ')

        if not how_many_passwords.isdigit():
            print('Введите натуральное числовое значение!')
        elif how_many_passwords == '0':
            print('Мы генерируем от одного пароля и больше')
        else:
            how_many_passwords = int(how_many_passwords)
            return how_many_passwords


def get_password_len(password_count):
    while True:
        if password_count == 1:
            password_len = input('Укажите длину пароля: ')
        else:
            password_len = input('Укажите длину паролей: ')

        if not password_len.isdigit():
            print('Введите натуральное числовое значение!')

        else:
            password_len = int(password_len)
            return password_len


def should_add_digits():
    while True:
        answer = input('Включать ли в пароль символы 0123456789? ').lower()
        if answer == 'да':
            has_digits = True
            return has_digits
        elif answer == 'нет':
            has_digits = False
            return has_digits
        else:
            print('Дайте ответ по типу "да/нет"')


def should_add_uppers():
    while True:
        answer = input('Включать ли в пароль символы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ').lower()
        if answer == 'да':
            has_uppers = True
            return has_uppers
        elif answer == 'нет':
            has_uppers = False
            return has_uppers
        else:
            print('Дайте ответ по типу "да/нет"')


def should_add_lowers():
    while True:
        answer = input('Включать ли в пароль символы abcdefghijklmnopqrstuvwxyz? ').lower()
        if answer == 'да':
            has_lowers = True
            return has_lowers
        elif answer == 'нет':
            has_lowers = False
            return has_lowers
        else:
            print('Дайте ответ по типу "да/нет"')


def should_add_spec_chars():
    while True:
        answer = input('Включать ли в пароль символы !#$%&*+-=?@^_ ? ').lower()
        if answer == 'да':
            has_punctuation = True
            return has_punctuation
        elif answer == 'нет':
            has_punctuation = False
            return has_punctuation
        else:
            print("Дайте ответ по типу \"да\нет\"")


def should_add_ambiguous_chars():
    while True:
        answer = input('Добавлять ли неоднозначные символы символы il1Lo0O ? ').lower()
        if answer == 'да':
            add_sym = True
            return add_sym
        elif answer == 'нет':
            add_sym = False
            return add_sym
        else:
            print('Дайте ответ по типу "да/нет"')


def sanitize_password_chars(should_add_digits: bool,
                            should_add_uppers: bool, should_add_lowers: bool, should_add_spec_chars: bool,
                            should_add_ambigeous_chars: bool):
    chars = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_!#$%&*+-=?@^_')

    if not should_add_digits:
        for char in '0123456789':
            chars.remove(char)

    if not should_add_uppers:
        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            chars.remove(char)

    if not should_add_lowers:
        for char in 'abcdefghijklmnopqrstuvwxyz':
            chars.remove(char)

    if not should_add_spec_chars:
        for char in '!#$%&*+-=?@^_!#$%&*+-=?@^_':
            chars.remove(char)

    if not should_add_ambigeous_chars:
        for char in 'il1Lo0O':
            chars.remove(char)

    return ''.join(chars)


def generate_password(password_len: int, chars: str):
    from random import choice
    password = ''

    for _ in range(password_len):
        password += choice(chars)

    return password
