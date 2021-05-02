
# Map each character in word to its height thru index. Then, find the maximum height
# At last, multiply with the length of word

def designerPdfViewer(h, word):
    return max( map(lambda c: h[ord(c) - ord('a')], word) ) * len(word)