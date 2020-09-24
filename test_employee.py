import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for Employee class"""

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    # For uniform instances use
    def setUp(self):
        self.levin = Employee('Levin', 'Batallones','2000000')
        self.martin = Employee('Martin', 'Briceno', '300000')
        self.adam = Employee('Adam', 'Honore', '200000')
        self.rome = Employee('Rome', 'Bell', '300000')

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        self.assertEqual(self.levin.email, 'levin.batallones@sei713.com')
        self.assertEqual(self.martin.email, 'martin.briceno@sei713.com')
        self.assertEqual(self.adam.email, 'adam.honore@sei713.com')
        self.assertEqual(self.rome.email, 'rome.bell@sei713.com')
   

    def test_fullname(self):
        self.assertEqual(self.adam.fullname, 'Adam Honore')
        self.assertEqual(self.rome.fullname, 'Rome Bell')
        self.assertEqual(self.levin.fullname, 'Levin Batallones')
        self.assertEqual(self.martin.fullname, 'Martin Briceno')

    def test_raise_amount(self):
        self.adam.apply_raise()
        self.rome.apply_raise()
        self.assertEqual(self.adam.pay, 230000)
        self.assertEqual(self.rome.pay, 345000)



# More info on unit testing here:
# https://docs.python.org/3/library/unittest.html





if __name__ == '__main__':
    unittest.main()