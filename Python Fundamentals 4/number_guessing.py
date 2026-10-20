secret=8
for i in range(5):
    n=int(input())
    if n==secret:
        print("Correct")
        break
    elif n<secret:
        print("Too Low")
    else:
        print("Too High")
else:
    print("Game Over")