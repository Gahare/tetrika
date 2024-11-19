import unittest
import solution

class TestStringMethods(unittest.TestCase):


    def test_validation(self):
        trueVariants = [3, 1, 20]
        falseVariants = [True, 5.1, "Hello"]
        for i in trueVariants:
            for j in falseVariants:
                print("Testing sum of " + str(i) + " and " + str(j))
                with self.assertRaises(TypeError):
                    result = solution.sum_two(i,j)
                if result == True:
                    print ("OK")
                
    """
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    """

if __name__ == '__main__':
    unittest.main()