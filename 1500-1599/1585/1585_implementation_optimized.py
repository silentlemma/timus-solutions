import sys

data = sys.stdin.buffer.read()
# every record is two words, the kind and "Penguin", so counting the full
# names in the raw bytes counts the records of each kind
names = (b"Emperor Penguin", b"Little Penguin", b"Macaroni Penguin")
print(max(names, key=data.count).decode())
