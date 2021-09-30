#language : Python2
def pharmacy():
    N = input()
    S = raw_input().strip()

    left = [None]*N
    curr = float("-inf")
    for i, c in enumerate(S):
        if c == '1':
            curr = i
        left[i] = curr
    result = 0
    curr = float("inf")
    for i in reversed(xrange(len(S))):
        if S[i] == '1':
            curr = i
        result += min(i-left[i], curr-i)
    return result

for case in xrange(input()):
    print '%s' % (pharmacy())
