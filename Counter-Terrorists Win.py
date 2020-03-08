import random

cipher = '144 122 135 134 139 88 64 116 133 114 129 120 111 138 66 20 146 64 101 194 121 64 127 132 117 64 194 114 135 64 202 126 210 216 64 198 222 200 202 64 222 220 64 242 222 234 228 64 230 202 228 236 202 228 64 116 136 20 120 126 160 144 160 20 64 64 64 64 202 236 194 216 80 72 190 142 138 168 182 78 198 222 218 218 194 220 200 190 204 222 228 190 202 240 202 240 234 232 202 78 186 82 118 118 20 64 64 64 64 94 94 64 178 138 88 64 134 158 154 154 130 156 136 158 164 66 66 66 66 20 126 124 20'


def encrypt(text):
    key = random.randint(1, len(text) * 2)
    result = []

    for c in text:
        result.append(ord(c) + (ord(c) % key))
        key += 1

    return result


def decrypt(code_list):
    texts = []

    for cur_key in range(1, len(code_list) * 2):
        key = cur_key
        decrypted_text = ''

        for code in code_list:
            for ascii_cur in range(0, 127):
                if ascii_cur + (ascii_cur % key) == code:
                    decrypted_text += chr(ascii_cur)
                    key += 1
                    break

        texts.append(decrypted_text)

    return texts


cipher_int_list = list(map(lambda x: int(x), cipher.split()))

for text in decrypt(cipher_int_list):
    print(text)
