def rotate(text, key):
    result = ""

    # Loop over characters.
    for char in text:
        # Convert to number with ord.
        char_byte = ord(char)

        # Shift number back or forward.
        if char_byte >= ord('a') and char_byte <= ord('z'):
            if char_byte > ord('m'):
                char_byte -= key
            else:
                char_byte += key
        elif char_byte >= ord('A') and char_byte <= ord('Z'):
            if char_byte > ord('M'):
                char_byte -= key
            else:
                char_byte += key

        # Append to result.
        result += chr(char_byte)

    # Return transformation.
    return result
