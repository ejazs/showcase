
class MyException(Exception):
  pass

# def exception_check(name):
#   if type(name)==int:
#     raise MyException('This is wrong type')
#   else:
#     print(name)

# exception_check(1)

def another_exception_check(name):
  try:
    if type(name)==int:
      raise MyException('Wow again?')
    else:
      print(name)
  except MyException as e:
    print('Yay this is good')

another_exception_check(1)

# def div(a,b):
#   return a/b

# print(div(1,2))