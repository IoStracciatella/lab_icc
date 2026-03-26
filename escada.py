import sys

vals = list(map(int, sys.stdin.read().split()))
if not vals:
    exit()
n = vals[0]
times = vals[1:1+n]
total = 0
end = -10**18
for t in times:
    if t >= end:
        total += 10
    else:
        total += (t + 10 - end)
    end = t + 10
print(total)
