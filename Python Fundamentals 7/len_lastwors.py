def length_of_last_word(s):
    return len(s.split()[-1]) if s.split() else 0
s=" Embedded Python "
print("Length of last word:",length_of_last_word(s))