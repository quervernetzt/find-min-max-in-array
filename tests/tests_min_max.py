import unittest
import random
from typing import List, Tuple
from solution.min_max import MinMax


class TestCasesMinMax(unittest.TestCase):
    def input_list_is_none_return_none_set(self: object) -> None:
        # Arrange
        min_max: MinMax = MinMax()
        input_list: List[int] = None

        # Act
        result: Tuple[int, int] = min_max.main(input_list)

        # Assert
        self.assertEqual(result, (None, None))

    def input_list_is_empty_return_none_set(self: object) -> None:
        # Arrange
        min_max: MinMax = MinMax()
        input_list: List[int] = []

        # Act
        result: Tuple[int, int] = min_max.main(input_list)

        # Assert
        self.assertEqual(result, (None, None))

    def input_list_has_element_not_int_return_type_error(self: object) -> None:
        # Arrange
        min_max: MinMax = MinMax()
        input_list: List[int] = [2, 3, 4, "test", 1, 9]

        # Act & Assert
        self.assertRaises(TypeError, min_max.main, input_list)

    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    def input_list_has_one_element_return_set_with_element(self: object) -> None:
        # Arrange
        min_max: MinMax = MinMax()
        input_list: List[int] = [2]

        # Act
        result: Tuple[int, int] = min_max.main(input_list)

        # Assert
        self.assertEqual(result, (2, 2))

    def input_list_has_multiple_elements_with_duplicates_return_set_with_min_max(self: object) -> None:
        # Arrange
        min_max: MinMax = MinMax()
        input_list: List[int] = [2, -1, 4, 5, -45, 4, 1, 300, -10, 2]

        # Act
        result: Tuple[int, int] = min_max.main(input_list)

        # Assert
        self.assertEqual(result, (-45, 300))

    def input_list_has_many_multiple_elements_return_set_with_min_max(self: object) -> None:
        # Arrange
        min_max: MinMax = MinMax()
        input_list: List[int] = [i for i in range(-10000, 1000000)]
        random.shuffle(input_list)

        # Act
        result: Tuple[int, int] = min_max.main(input_list)

        # Assert
        self.assertEqual(result, (-10000, 999999))
