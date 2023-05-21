def vote(votes):
    d = {}
    for v in votes:
        d.setdefault(v, 0)
        d[v] += 1
    print(d)
    sorted_by_count = sorted(d.items(), key=lambda a: a[1], reverse=True)
    print(sorted_by_count)
    return sorted_by_count[0][0]



