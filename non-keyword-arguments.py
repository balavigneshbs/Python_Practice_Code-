# def my_function(a,b,c):
#     print("the number is "  +  c)
# my_function(a="1" ,b="2" ,c="3") 

def func(**bala):
    print(bala.get('a'))

func(a=1, b=2, c=3, j=7)

def func1(*var):
    print(list(var))

func1(1,2,3)
