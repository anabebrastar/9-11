import unittest
from funcs import rotate_matrix, sum_large_numbers, count_subarrays_with_sum

class TestFunctions(unittest.TestCase):

    def test_rotate_matrix_clockwise(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        result = rotate_matrix(matrix, 'clockwise')
        self.assertEqual(result, expected)

    def test_rotate_matrix_counterclockwise(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7]
        ]
        result = rotate_matrix(matrix, 'counterclockwise')
        self.assertEqual(result, expected)

    def test_sum_large_numbers(self):
        array1 = [1, 2, 3]
        array2 = [4, 5, 6]
        expected_sum = [5, 7, 9]
        expected_difference = [-3, -3, -3]
        result_sum = sum_large_numbers(array1, array2, 'sum')
        result_difference = sum_large_numbers(array1, array2, 'difference')
        self.assertEqual(result_sum, expected_sum)
        self.assertEqual(result_difference, expected_difference)

    def test_count_subarrays_with_sum(self):
        array = [1, 2, 3, 4]
        target_sum = 6
        expected = 1  # Подмассивы: [2, 4]
        result = count_subarrays_with_sum(array, target_sum)
        print (result)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
