def findTheTownJudge(n, trust):
    persons = []
    for i in range(n):
        persons.append({"person": i + 1, "trusted_by": 0, "trusts": 0})
    for v in trust:
        persons[v[0] - 1]["trusts"] += 1
        persons[v[1] - 1]["trusted_by"] += 1

    for p in persons:
        if p["trusts"] == 0 and p["trusted_by"] == n - 1:
            return p["person"]
    return -1

n = 4
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
print(findTheTownJudge(n, trust))
