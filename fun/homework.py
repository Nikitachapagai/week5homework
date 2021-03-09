def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    if incoming_list is None or len(incoming_list) == 0:
        return 0
    else:
        return max(incoming_list)


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    if incoming_list is None or len(incoming_list) == 0:
        return 0
    else:
        return min(incoming_list)


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    if incoming_list is None or len(incoming_list) == 0:
        return 0
    else:
        return sum(incoming_list)


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    if incoming_dict is None or len(incoming_dict) == 0:
        return None
    return max(incoming_dict, key=lambda value: len(incoming_dict[value]))
