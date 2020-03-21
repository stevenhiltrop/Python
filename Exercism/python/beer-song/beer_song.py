def recite(start, take=1):
    lyrics = list()
    for bottle in range(start, start - take, -1):
        remainder = bottle - 1
        if remainder <= 0:
            remainder = "no more"
            start = 99
        lyrics.append(f"{bottle} bottles of beer on the wall, {bottle} bottles of beer.")
        lyrics.append(f"Take one down and pass it around, {remainder} bottles of beer on the wall.")
    return lyrics
