def slices(series, length):
    return list(series[x:length + x] for x in range(len(series)) if len(series[x:length + x]) == length)
