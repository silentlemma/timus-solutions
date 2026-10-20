import heapq
import sys


def main():
    data = sys.stdin.buffer.read().split()
    keyword_count = int(data[0])
    words = data[2 : 2 + keyword_count]
    indices = {word: vertex for vertex, word in enumerate(words)}
    graph = [[] for _ in words]

    def word_id(word):
        vertex = indices.get(word)
        if vertex is None:
            vertex = len(words)
            indices[word] = vertex
            words.append(word)
            graph.append([])
        return vertex

    for position in range(2 + keyword_count, len(data), 2):
        source = word_id(data[position])
        target = word_id(data[position + 1])
        graph[source].append(target)
    del data

    needed = list(range(keyword_count))
    required = bytearray(len(words))
    for vertex in needed:
        required[vertex] = 1
    indegree = [0] * len(words)

    # Appending during this traversal discovers exactly the mandatory words.
    for vertex in needed:
        for target in graph[vertex]:
            indegree[target] += 1
            if not required[target]:
                required[target] = 1
                needed.append(target)

    ready = [(words[vertex], vertex) for vertex in needed if indegree[vertex] == 0]
    heapq.heapify(ready)
    answer = []
    while ready:
        word, vertex = heapq.heappop(ready)
        answer.append(word)
        for target in graph[vertex]:
            indegree[target] -= 1
            if indegree[target] == 0:
                heapq.heappush(ready, (words[target], target))

    if len(answer) != len(needed):
        sys.stdout.buffer.write(b"-1\n")
    else:
        sys.stdout.buffer.write(b" ".join(answer) + b"\n")


if __name__ == "__main__":
    main()
