from exceptions import PathError


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError as exception:
            return f"Key Error - {exception}, Ви ввели невірне ім'я"
        except ValueError as exception:
            return exception.args[0]
        except TypeError:
            return "Помилкова команда"
        except IndexError:
            return "Вводити потрібно (Ім'я та наступна інформація)"
        except PathError:
            return "Потрібно ввести корректний шлях до папки."
    return wrapper
