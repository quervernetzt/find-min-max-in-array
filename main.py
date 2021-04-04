import random
from typing import List, Tuple
from tests.tests_min_max import TestCasesMinMax
from solution.min_max import MinMax

if __name__ == "__main__":
    ###################################
    # Tests
    ###################################
    tests_min_max: TestCasesMinMax = TestCasesMinMax()

    tests_min_max.input_list_is_none_return_none_set()
    tests_min_max.input_list_is_empty_return_none_set()
    tests_min_max.input_list_has_element_not_int_return_type_error()

    tests_min_max.input_list_has_one_element_return_set_with_element()
    tests_min_max.input_list_has_multiple_elements_with_duplicates_return_set_with_min_max()
    tests_min_max.input_list_has_many_multiple_elements_return_set_with_min_max()

    ###################################
    # Demo
    ###################################
    min_max: MinMax = MinMax()

    input_list: List[int] = [i for i in range(-10, 10000)]
    random.shuffle(input_list)
    result: Tuple[int, int] = min_max.main(input_list)
    print(result)  # (-10, 9999)
