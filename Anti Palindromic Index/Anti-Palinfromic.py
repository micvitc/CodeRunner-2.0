#language : Python2
def anti_palindromic():
    N, K = map(int, raw_input().strip().split())
    S = raw_input().strip()

    return abs(sum(int(S[i] != S[N-1-i]) for i in xrange(N//2))-K)

for case in xrange(input()):
    print '%s' % (anti_palindromic())
