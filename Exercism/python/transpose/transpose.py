def transpose(lines):
    if lines:
        result = [''.join(tup) for tup in (zip(*lines.splitlines()))]
        return '\n'.join(result)
    else:
        return lines
