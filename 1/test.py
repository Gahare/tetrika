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
        for i in falseVariants:
            for j in falseVariants:
                print("Testing sum of " + str(i) + " and " + str(j))
                with self.assertRaises(TypeError):
                    result = solution.sum_two(i,j)
        for i in trueVariants:
            for j in trueVariants:
                print("Testing sum of " + str(i) + " and " + str(j))
                self.assertEqual(solution.sum_two(i,j),i+j)

if __name__ == '__main__':
    unittest.main()