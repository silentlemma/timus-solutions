pages, cover, first, last = map(int, open(0, "rb").read().split())
distance = abs(last - first) * (pages + 2 * cover)
print(distance - pages if first < last else distance + pages)
