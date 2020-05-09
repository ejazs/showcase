class Person:

  def __new__(cls, *args):
    return super(Person, cls).__new__(cls)

  def __init__(self, name, age):
    self.name = name
    self.age  = age
    self.email = '{}@company.com'.format(name)

  @property
  def get_name(self):
    return self.name

  @get_name.setter
  def set_name(self, name):
    self.name = name

  def get_email(self):
    return self.email

  def __str__(self):
    return str(self.name)
  
  def __repr__(self):
    return str(self.name)

  # def __del__(self):
  #   raise NameError('cannot delete')
  #   return False
  #   print('Del called')

a = Person('Mac', 23)
print(a.get_name)
a.set_name = 'Mak'
print(a.get_name)
print(a.get_email())
# del a
# print(a.get_name)