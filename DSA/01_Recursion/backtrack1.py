# print linearly from 1 to N (but by backtracking)
# should not use (i+1,n)


def back_Track(i,n):
    if i<1:
        return
    back_Track(i-1,n)
    print(i)

n = int(input("enter a number"))

back_Track(n,n)

# print linearly from N to 1 (but by backtracking)
# do not use (i-1,n)

def back_track(i,n):
    if i>n:
        return
    back_track(i+1,n)
    print(i)

n = int(input("enter a num"))

back_track(1,n)