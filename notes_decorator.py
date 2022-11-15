def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError as e:
            return (f"Key Error - Note with id[{e}] doesn't exist")
        except ValueError as e:
            return (f"Value Error - {e}")
    return wrapper