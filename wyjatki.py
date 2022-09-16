import logging


def mnozenie(a, b):
    try:
        return int(a) * int(b)
    # except Exception:
    except TypeError:
        return logging.warning("Błąd nr 723634: nie da się tak!")
    except ValueError:
        return logging.warning("Błąd nr 859658: nie da się tak!")


def mnozenie2(a, b):
    return a * b


invalid_dict = [{'name': 'Jan', 'age': 'sss'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]


def check_age(users, age):
    count = 0
    for i, user in enumerate(users):
        try:
            user_age = int(user['age'])
        except KeyError:
            print('niepoprawne dane: {}'.format(user))
        except ValueError:
            print('niepoprawny wiek: {}'.format(user))
        else:
            count += 1 if user_age < age else 0
        finally:
            print("{}, {}".format(i, user))
    return count


print(check_age(invalid_dict, 18))

# print(mnozenie('a', 'b'))  # value
# print(mnozenie('5', '10'))  # ok
# print(mnozenie(None, 3))  # type

# try:
#     mnozenie2('a', 'b')
# except TypeError:
#     logging.warning("Błąd nr 72363472: nie da się tak!")
