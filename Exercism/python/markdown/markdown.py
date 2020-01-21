import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    single_underscore = '(.*)_(.*)_(.*)'
    double_underscore = '(.*)__(.*)__(.*)'
    for line in lines:
        # if line.startswith('#'):
        #     header = line.count('#')
        #     line = '<h' + header + '>' + line[header + 1:] + '</h' + header + '>'
        if re.match('###### (.*)', line) is not None:
            line = '<h6>' + line[7:] + '</h6>'
        elif re.match('## (.*)', line) is not None:
            line = '<h2>' + line[3:] + '</h2>'
        elif re.match('# (.*)', line) is not None:
            line = '<h1>' + line[2:] + '</h1>'
        regex_match = re.match(r'\* (.*)', line)
        if regex_match:
            curr = regex_match.group(1)
            single_underscore__match = re.match(single_underscore, curr)
            double_underscore__match = re.match(double_underscore, curr)
            if not in_list:
                in_list = True

                if double_underscore__match:
                    curr = double_underscore__match.group(1) + '<strong>' + \
                           double_underscore__match.group(2) + '</strong>' + double_underscore__match.group(3)

                if single_underscore__match:
                    curr = single_underscore__match.group(1) + '<em>' + single_underscore__match.group(2) + \
                           '</em>' + single_underscore__match.group(3)
                line = '<ul><li>' + curr + '</li>'
            else:
                if double_underscore__match:
                    curr = double_underscore__match.group(1) + '<strong>' + \
                           double_underscore__match.group(2) + '</strong>' + double_underscore__match.group(3)
                if single_underscore__match:
                    curr = single_underscore__match.group(1) + '<em>' + single_underscore__match.group(2) + \
                           '</em>' + single_underscore__match.group(3)
                line = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        regex_match = re.match('<h|<ul|<p|<li', line)
        if not regex_match:
            line = '<p>' + line + '</p>'
        regex_match = re.match(double_underscore, line)
        if regex_match:
            line = regex_match.group(1) + '<strong>' + regex_match.group(2) + '</strong>' + regex_match.group(3)
        regex_match = re.match(single_underscore, line)
        if regex_match:
            line = regex_match.group(1) + '<em>' + regex_match.group(2) + '</em>' + regex_match.group(3)
        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        res += line
    if in_list:
        res += '</ul>'
    return res
