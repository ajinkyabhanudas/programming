import os
import sys

path = os.path.join(os.path.dirname(__file__), '..', 'questions_easy')
sys.path.append(path)

import two_sum

class TestTwoSum():

    @staticmethod
    def test_all_positives():
        input_list = [2, 7, 11, 15]
        target = 26
        result = two_sum.Solution.two_sum(input_list, target)
        assert input_list[result[0]] + input_list[result[1]] == target

    @staticmethod
    def test_all_negatives():
        input_list = [-2, -8, -1, -99]
        target = -9
        result = two_sum.Solution.two_sum(input_list, target)
        assert input_list[result[0]] + input_list[result[1]] == target

    @staticmethod
    def test_mixed():
        input_list = [-19, 123, -170, 177]
        target = 7
        result = two_sum.Solution.two_sum(input_list, target)
        assert input_list[result[0]] + input_list[result[1]] == target