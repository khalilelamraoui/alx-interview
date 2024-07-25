#!/usr/bin/python3
"""Function that validates the UTF8 encoding"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Loop over each integer in the data list
    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1's in the byte
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # If it's a 1-byte character
            if num_bytes == 0:
                continue

            # For UTF-8, num_bytes should be between 2 and 4
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If this byte does not start with 10, it's not valid
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    # If there are leftover bytes that we were expecting, it's not valid
    return num_bytes == 0
