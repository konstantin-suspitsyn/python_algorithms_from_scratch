from typing import Optional


class SearchAlgorithms:
    """
    Creating standard algorithms for studying purposes
    """

    @staticmethod
    def __compare_letter_by_letter(base_str: str, str_to_compare: str) -> tuple[bool, Optional[str]]:
        """
        Compares base_str with str_to_compare sign by sign
        :param base_str: string to compare. Should be lower_case
        :param str_to_compare: string to compare with. Should be lower_case
        :return: [True if base_str == str_to_compare, None]
                 [False if base_str == str_to_compare, "->" if letter in base_str > letter in str_to_compare
                                                     , "<-" if letter in base_str < letter in str_to_compare]
        """

        assert base_str.islower(), "{} should be lowercase".format(base_str)
        assert str_to_compare.islower(), "{} should be lowercase".format(str_to_compare)

        min_str_length = min(len(base_str), len(str_to_compare))

        if base_str == str_to_compare:
            return True, None

        elif base_str[:min_str_length] == str_to_compare[:min_str_length]:
            # If smaller part of one string == same part of another string
            if len(base_str) > len(str_to_compare):
                return False, "->"
            else:
                return False, "<-"
        else:
            for number_of_letter in range(min_str_length):
                if base_str[number_of_letter] > str_to_compare[number_of_letter]:
                    return False, "->"

                elif base_str[number_of_letter] < str_to_compare[number_of_letter]:
                    return False, "<-"

    @staticmethod
    def binary_search_of_string(str_to_search: str, sorted_list: list) -> str:
        """
        Binary search string in a sorted list

        :param str_to_search: string to search
        :param sorted_list: list of strings, sorted a->z lowercase
        :return: string
        """
        assert isinstance(str_to_search, str), "Should be string"
        assert isinstance(sorted_list, list), "Should be list"

        steps_counter = 0

        lower_str_to_search = str_to_search.lower()

        flag = False
        success = False

        fail_message = "Perfect match was NOT found\n"\
                       "I've searched for {} in list of {} items. {} steps done"
        success_message = "Perfect match WAS found on position {}\n"\
                          "I've searched for {} in list of {} items. {} steps were done"

        start = 0
        middle = len(sorted_list) // 2
        end = len(sorted_list) - 1

        while not flag:

            steps_counter += 1

            str_to_compare = str(sorted_list[middle]).lower()
            result = SearchAlgorithms.__compare_letter_by_letter(lower_str_to_search, str_to_compare)

            if start == middle and middle == end and not result[0]:
                flag = True

            if result[0]:
                # We found perfect match
                position = middle
                success = True
                break
            elif not result[0]:
                if result[1] == "->":
                    start = min(middle + 1, end)
                    middle = (end - start) // 2 + start
                elif result[1] == "<-":
                    end = max(middle - 1, start)
                    middle = (end - start) // 2 + start

        if success:
            return success_message.format(position, str_to_search, len(sorted_list), steps_counter)
        if not success:
            return fail_message.format(str_to_search, len(sorted_list), steps_counter)


if __name__ == "__main__":
    with open(r"data/oscar_movies.txt", "r") as file:
        sorted_oscar_movies = file.read().splitlines()
        file.close()

    print(SearchAlgorithms.binary_search_of_string("Random Name", sorted_oscar_movies))
