import sys


SMALL_SIZE = 16


def count_segments(values):
    size = len(values)
    value_limit = max(values)
    last = [-1] * (value_limit + 1)
    first = [0] * size
    boundary = 0
    for index, value in enumerate(values):
        if boundary <= last[value]:
            boundary = last[value] + 1
        first[index] = boundary
        last[value] = index

    last = [size] * (value_limit + 1)
    final = [0] * size
    boundary = size - 1
    for index in range(size - 1, -1, -1):
        value = values[index]
        if boundary >= last[value]:
            boundary = last[value] - 1
        final[index] = boundary
        last[value] = index

    low = [0] * size
    high = [0] * size
    minimum_counts = [0] * (size + value_limit + 1)
    maximum_counts = [0] * (size + value_limit + 1)

    def solve(left, right):
        if right - left < SMALL_SIZE:
            answer = right - left + 1
            for start in range(left, right):
                smallest = largest = values[start]
                stop = final[start]
                if stop > right:
                    stop = right
                for end in range(start + 1, stop + 1):
                    value = values[end]
                    if value < smallest:
                        smallest = value
                    elif value > largest:
                        largest = value
                    if largest - smallest == end - start:
                        answer += 1
            return answer
        middle = (left + right) // 2
        answer = solve(left, middle) + solve(middle + 1, right)
        if left < first[middle + 1]:
            left = first[middle + 1]
        if right > final[middle]:
            right = final[middle]
        if left > middle or right <= middle:
            return answer

        smallest = largest = values[middle]
        for index in range(middle, left - 1, -1):
            value = values[index]
            if value < smallest:
                smallest = value
            elif value > largest:
                largest = value
            low[index] = smallest
            high[index] = largest
        smallest = largest = values[middle + 1]
        for index in range(middle + 1, right + 1):
            value = values[index]
            if value < smallest:
                smallest = value
            elif value > largest:
                largest = value
            low[index] = smallest
            high[index] = largest

        # Each upper bound first grows, then shrinks as duplicate limits decrease.
        # New endpoints are filtered by the lower bound only while the window is nonempty.
        min_left = max_left = middle + 1
        min_right = max_right = middle
        min_limit = max_limit = middle
        for index in range(middle, left - 1, -1):
            smallest = low[index]
            largest = high[index]
            end = index + largest - smallest
            if (
                middle < end <= right
                and end <= final[index]
                and high[end] < largest
                and low[end] > smallest
            ):
                answer += 1

            # The maximum is on the left.
            while min_limit < right and high[min_limit + 1] < largest:
                min_limit += 1
            end = min_limit
            if end > final[index]:
                end = final[index]
            if end > min_right:
                for position in range(min_right + 1, end + 1):
                    minimum_counts[low[position] + position] += 1
            elif end < min_right:
                begin = end + 1
                if begin < min_left:
                    begin = min_left
                for position in range(begin, min_right + 1):
                    minimum_counts[low[position] + position] -= 1
            min_right = end
            while min_left <= end and low[min_left] >= smallest:
                minimum_counts[low[min_left] + min_left] -= 1
                min_left += 1
            answer += minimum_counts[largest + index]

            # The minimum is on the left.
            while max_limit < right and low[max_limit + 1] > smallest:
                max_limit += 1
            end = max_limit
            if end > final[index]:
                end = final[index]
            if end > max_right:
                for position in range(max_right + 1, end + 1):
                    maximum_counts[high[position] - position + size] += 1
            elif end < max_right:
                begin = end + 1
                if begin < max_left:
                    begin = max_left
                for position in range(begin, max_right + 1):
                    maximum_counts[high[position] - position + size] -= 1
            max_right = end
            while max_left <= end and high[max_left] <= largest:
                maximum_counts[high[max_left] - max_left + size] -= 1
                max_left += 1
            answer += maximum_counts[smallest - index + size]

        for end in range(middle + 1, right + 1):
            start = end - high[end] + low[end]
            if (
                left <= start <= middle
                and end <= final[start]
                and high[start] < high[end]
                and low[start] > low[end]
            ):
                answer += 1
        for position in range(min_left, min_right + 1):
            minimum_counts[low[position] + position] = 0
        for position in range(max_left, max_right + 1):
            maximum_counts[high[position] - position + size] = 0
        return answer

    return solve(0, size - 1)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    print(count_segments(data[1:]))


if __name__ == "__main__":
    main()
