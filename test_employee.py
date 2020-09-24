import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for Employee class"""

    def test_email(self):
        levin = Employee('Levin', 'Batallones','2000000')
        martin = Employee('Martin', 'Briceno', '300000')

        self.assertEqual(levin.email, 'levin.batallones@sei713.com')
        self.assertEqual(martin.email, 'martin.briceno@sei713.com')
   

    def test_fullname(self):
        adam = Employee('Adam', 'Honore', '200000')
        rome = Employee('Rome', 'Bell', '300000')
        self.assertEqual(adam.fullname, 'Adam Honore')
        self.assertEqual(rome.fullname, 'Rome Bell')


# More info on unit testing here:
# https://docs.python.org/3/library/unittest.html





if __name__ == '__main__':
    unittest.main()