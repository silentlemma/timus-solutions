from sys import stdin, stdout

length, total, speed_a, speed_b = map(int, stdin.readline().split())
intervals = int(stdin.readline())
ridden = (speed_a + speed_b) * total
# Nonoverlapping stops subtract only their durations from monotone
# relative distance; a shared stationary meeting is counted just once.
for _ in range(intervals):
    rider, _, duration = map(int, stdin.readline().split())
    ridden -= (speed_a if rider == 1 else speed_b) * duration
stdout.write(str(ridden // length))
