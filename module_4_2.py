
def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()
#inner_function() 'это функция внутренняя. Она не в области видемости. Она не сработает т.к. она как будто не существует.
