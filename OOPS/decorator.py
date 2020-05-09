'''
  Decorators provide a way of adding new functionality to existing functions without changing
  the original code/function

'''

def authenticated(func):
  '''
  This is the example of basic Decorator with no args for inner function.
  All func calls are unexecuted except func passed.
  '''
  def wrapper_func():
    print('Execute extra code here')
    return func()
  
  return wrapper_func

@authenticated
def normal_func():
  return 'We return text'

call = normal_func()
print(call)


def authenticated_with_args(func):
  '''
  This is the example of basic Decorator with args for inner function.
  All func calls are unexecuted except func passed.
  '''
  def wrapper_func(*args, **kwargs):
    print('Extra code here')
    return func(*args, **kwargs)
  return wrapper_func

@authenticated_with_args
def normal_func_with_params(name):
  return 'Welcome Mr.{}'.format(name)

call = normal_func_with_params('Ejaz')
print(call)


def authenticated_with_args_and_params(param):
  '''
  This is the example of basic Decorator with args and params for inner function.
  All func calls are unexecuted except func passed.
  '''
  def outer_wrapper(func):
    def inner_wrapper(*args, **kwargs):
      print('Extra code here, param is :{}'.format(param))
      return func(*args, **kwargs)
    return inner_wrapper
  return outer_wrapper


@authenticated_with_args_and_params('PARAM')
def normal_func_with_params(name):
  return 'Welcome Mr.{}'.format(name)

call = normal_func_with_params('Shaikh')
print(call)
