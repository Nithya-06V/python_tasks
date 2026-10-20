s=input()
u=l=d=sp=False
for c in s:
    if c.isupper():
        u=True
    elif c.islower():
        l=True
    elif c.isdigit():
        d=True
    else:
        sp=True
print("Valid password" if len(s)>=8 and u and l and d and sp else "Invalid password")
print("Uppercase:", "Present" if u else "Missing")
print("Lowercase:", "Present" if l else "Missing")
print("Digit:", "Present" if d else "Missing")
print("Special character:", "Present" if sp else "Missing")
print("Minimum length:", "Satisfied" if len(s)>=8 else "Not satisfied")