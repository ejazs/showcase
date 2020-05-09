from person import Person
import unittest
class TestPerson(unittest.TestCase):

  def setUp(self):
    self.person = Person('Salmon Boi', 48)

  def test_obj_created(self):
    self.assertEqual(str(self.person), 'Salmon Boi')
  
  def test_correct_get_name(self):
    self.assertEqual(self.person.get_name, 'Salmon Boi')
  
  def test_correct_get_email(self):
    self.assertEqual(self.person.get_email(), 'Salmon Boi@company.com')


if __name__ == '__main__':
  unittest.main()
