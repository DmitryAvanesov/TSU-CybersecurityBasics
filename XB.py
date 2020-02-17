hex_numbers = '4E 6D 4E 6B 4D 7A 55 31 4E 6D 52 6C 59 6A 42 6B 59 54 55 30 59 6D 4E 68 4D 44 59 77 59 6A 52 6A 4D 7A 6B 30 4E 7A 6B 34 4D 7A 6B 3D'
hex_numbers_array = hex_numbers.split()
dec_numbers_array = []

for i in hex_numbers_array:
    dec_numbers_array.append(str(chr(int(i, 16))))

dec_numbers = ''.join(dec_numbers_array)

print(dec_numbers)