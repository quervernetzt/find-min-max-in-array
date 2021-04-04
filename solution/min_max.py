from typing import List, Tuple


class MinMax:
    def __init__(self: object) -> None:
        """Constructor.
        """
        pass

    def main(self: object, input_list: List[int]) -> Tuple[int, int]:
        """Get min and max from a list of integers in one traversal.

            Parameters
            ----------
            input_list : List[int], required
                List with integers.

            Returns
            ----------
            list
                Returns min and max and tuple.
        """

        if not input_list:
            return (None, None)

        min: int = None
        max: int = None

        for number in input_list:
            if not isinstance(number, int):
                raise TypeError("Only integers are allowed...")

            if not min:
                min = number
                max = number
            else:
                if number > max:
                    max = number
                if number < min:
                    min = number

        return (min, max)
