from random import choice, randint, shuffle


def make_one_special_char():
    # criar caractere especial baseado na tabela unicode
    # Ranges: 32-47 58-64 91-96 123-126 -> [ -\/:-@\[-`{-~]
    char_ranges = [
        randint(32, 47),
        randint(58, 64),
        randint(91, 96),
        randint(123, 126)
    ]

    return chr(choice(char_ranges))


def make_one_uppercase_letter():
    return chr(randint(65, 90))


def make_one_lowercase_letter():
    return chr(randint(97, 122))


def make_one_number():
    return chr(randint(48, 57))


def make_password(
    lengthy=16, chars=True, lower=True, upper=True, numbers=True
):
    assert isinstance(lengthy, int), 'length must be of type int'
    assert lengthy >= 4, 'length must be at least 4 chras'
    assert chars or lower or upper or numbers, 'At least one must be True'

    new_password = []

    for i in range(lengthy):
        chars and new_password.append(make_one_special_char())
        lower and new_password.append(make_one_lowercase_letter())
        upper and new_password.append(make_one_uppercase_letter())
        numbers and new_password.append(make_one_number())

    new_password = new_password[:lengthy]

    # embaralha os caracteres
    shuffle(new_password)

    return ''.join(new_password)


if __name__ == '__main__':
    print('\033[1m\033[94mPADRÃO\033[0m')
    for i in range(2):
        print(make_password())
    print()

    print('\033[1m\033[94mSEM CARACTERES ESPECIAIS\033[0m')
    for i in range(2):
        print(make_password(chars=False))
    print()

    print('\033[1m\033[94mSEM UPPER\033[0m')
    for i in range(2):
        print(make_password(upper=False))
    print()

    print('\033[1m\033[94mSEM LOWER\033[0m')
    for i in range(2):
        print(make_password(lower=False))
    print()

    print('\033[1m\033[94mAPENAS LOWER\033[0m')
    for i in range(2):
        print(make_password(
            chars=False, upper=False, numbers=False, lower=True
        ))
    print()

    print('\033[1m\033[94mAPENAS UPPER\033[0m')
    for i in range(2):
        print(make_password(
            chars=False, upper=True, numbers=False, lower=False
        ))
    print()

    print('\033[1m\033[94mAPENAS NUM\033[0m')
    for i in range(2):
        print(make_password(
            chars=False, upper=False, numbers=True, lower=False
        ))
    print()

    print('\033[1m\033[94mAPENAS CARACTERES ESPECIAIS\033[0m')
    for i in range(2):
        print(make_password(lengthy=16, chars=True,
                            upper=False, numbers=False, lower=False))
    print()
