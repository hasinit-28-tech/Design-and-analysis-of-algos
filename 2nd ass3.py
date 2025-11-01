import random

def to_binary(num):
    "Convert an integer to its binary (base-2) form as a string."
    if num == 0:
        return "0"

    bits = ""
    while num > 0:
        bits = str(num % 2) + bits 
        num //= 2
    return bits


def check_random_bit(num):
    "Pick a random bit from the binary form and tell if it’s 0 or 1."
    binary = to_binary(num)
    bit_length = len(binary)

    position = random.randint(0, bit_length - 1)

    bit_from_right = binary[::-1][position]

    print(f"Number: {num}")
    print(f"Binary form: {binary}")
    print(f"Random position chosen (from right): {position}")
    print(f"Bit at that position: {bit_from_right}")

    if bit_from_right == '1':
        print("That bit is 1 → TRUE")
    else:
        print("That bit is 0 → FALSE")


# Example:
random.seed(1) 
check_random_bit(37)  
