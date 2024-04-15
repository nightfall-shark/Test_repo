
def decorator(func):
    def wrap(*args, **kwargs):  # Определние выполняемой функции
        print('Gambler')
        func() # Вызов функции декоратора
        return 0
    return wrap

@decorator
def main():
    print('HEL')





if __name__=="__main__":
    main()