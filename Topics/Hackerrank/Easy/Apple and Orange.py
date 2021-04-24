
# Simply add each offset to a and b, and check if it is in range
# of [s,t]

def countApplesAndOranges(s, t, a, b, apples, oranges):
    inapples, inoranges = 0, 0
    for da in apples:
        inapples += 1 if s <= a + da <= t else 0
    for do in oranges:
        inoranges += 1 if s <= b + do <= t else 0
    print(inapples, inoranges, sep='\n')
