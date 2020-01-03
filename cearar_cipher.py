import enchant

words = enchant.Dict('en_US')

def auto_crack(text):
    for i in range(28):
        s = decrypt(i, text)
        string_array = s.split(' ')
        real_word = 0
        for word in string_array:
            if word:
                if words.check(word):
                    real_word += 1
        if real_word / len(string_array) > 0.8:
            return s

def encrypt(key,text):
    text = text.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz '
    encrypted_text = ''
    for char in text:
        index = letters.find(char)
        encrypted_text += letters[(index + key)%len(letters)]
    return encrypted_text


def decrypt(key, encrypted_text):
    return encrypt(-key, encrypted_text)

if __name__ == "__main__":
    text = encrypt(6, 'well that was hard, I want to go home now')
    results = auto_crack(text)
    
    print(results)