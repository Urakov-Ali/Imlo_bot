a = 'ali vali gani '
words = a
b = list(words.split())
while b:
    if len(b) > 1:
        for word in b:
            b.remove(word)
            print (b)