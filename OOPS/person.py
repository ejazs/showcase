class Employee(object):
  object_count = 0
  salary_raise = 10

  def __new__(cls, *args, **kwargs):
    if cls.object_count>4:
      raise TypeError('Cannot create more objects')
    cls.object_count+=1
    # return object.__new__(cls)
    return super(Employee, cls).__new__(cls)
  def __init__(self, name, email, salary):
    self.name = name
    self.email = email
    self.salary = salary

  @property
  def get_name(self):
    return self.name

  @get_name.setter
  def set_name(self, name):
    self.name = name
  
  @get_name.deleter
  def delete_name(self):
    self.name=None

  @classmethod
  def raise_amount(cls, salary):
    cls.raise_amount += salary

  @classmethod
  def new_init(cls, data):
    name, email, salary = data.split(',')
    return cls(name, email, salary)

  def __str__(self):
    return str(self.name)

  def __add__(self, other):
    return '{} {}'.format(str(self.name), str(other.name))
    

  def __repr__(self):
    return 'em = Employee("test name", "testname@example.com",21000)'
  
  @staticmethod
  def sum(a,b):
    return a+b
  


a = Employee('Major Toto', 'Major@toto.com', 21000)
b = Employee('Minor Momo', 'Major@toto.com', 21000)
print(a+b)

print(a.sum(10,20))

ehaz = Employee.new_init('Ejaz Shaikh,ejaz@ec-mobilit.biz, 10011')
print(ehaz.salary)