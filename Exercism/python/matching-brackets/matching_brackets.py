def is_paired(input_string: str) -> bool:
    return input_string.count('(') - input_string.count(')') == 0 and \
           input_string.count('{') - input_string.count('}') == 0 and \
           input_string.count('[') - input_string.count(']') == 0
