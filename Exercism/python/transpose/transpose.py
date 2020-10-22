def transpose(lines):
    if lines:
        return [''.join(tup) for tup in (zip(*lines))]
    else:
        return lines
