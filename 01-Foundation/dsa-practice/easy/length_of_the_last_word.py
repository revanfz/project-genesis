# Kembalikan panjang dari kata terkahir dari string yang diberikan
def length_of_the_last_word(s: str):
    clean_text = s.strip()
    for i, char in enumerate(clean_text[::-1]):
        if char == " ":
            return i
            
    return len(clean_text)

print(length_of_the_last_word("Hello World"))