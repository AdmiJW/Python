
# Simply keep a max score and min score counter.
# Everytime the record is broken, increment counter

def breakingRecords(scores):
    maxscore, maxbreak = scores[0], 0
    minscore, minbreak = scores[0], 0
    for s in scores:
        if s > maxscore:
            maxscore, maxbreak = s, maxbreak + 1
        elif s < minscore:
            minscore, minbreak = s, minbreak + 1
    return maxbreak, minbreak