#language : Python2
def game():
    S, F = [map(lambda x: ord(x)-ord('a'), list(raw_input().strip())) for _ in xrange(2)]
    dist = {c:min(min(abs(f-c), 26-abs(f-c)) for f in F) for c in xrange(26)}
    return sum(dist[c] for c in S)

for case in xrange(input()):
    print '%s' % (game())
