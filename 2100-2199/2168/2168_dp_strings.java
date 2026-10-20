import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int ALPHABET_SIZE = 26;
    private static final char FIRST_LETTER = 'a';

    private static String nextToken(BufferedInputStream input) throws IOException {
        StringBuilder token = new StringBuilder();
        int value;
        do {
            value = input.read();
        } while (value >= 0 && Character.isWhitespace(value));
        while (value >= 0 && !Character.isWhitespace(value)) {
            token.append((char) value);
            value = input.read();
        }
        return token.toString();
    }

    private static int[] suffixArray(String text) {
        int n = text.length();
        int length = n + 1;
        int[] symbols = new int[length];
        for (int i = 0; i < n; ++i) {
            symbols[i] = text.charAt(i) - FIRST_LETTER + 1;
        }
        int[] order = new int[length];
        int[] classes = new int[length];
        int[] shifted = new int[length];
        int[] nextClasses = new int[length];
        int[] counts = new int[Math.max(length, ALPHABET_SIZE + 1)];
        for (int symbol : symbols) {
            ++counts[symbol];
        }
        for (int i = 1; i < counts.length; ++i) {
            counts[i] += counts[i - 1];
        }
        for (int i = length - 1; i >= 0; --i) {
            order[--counts[symbols[i]]] = i;
        }
        int classCount = 1;
        for (int i = 1; i < length; ++i) {
            if (symbols[order[i]] != symbols[order[i - 1]]) {
                ++classCount;
            }
            classes[order[i]] = classCount - 1;
        }
        for (int shift = 1; shift < length && classCount < length; shift *= 2) {
            for (int i = 0; i < length; ++i) {
                shifted[i] = order[i] - shift;
                if (shifted[i] < 0) {
                    shifted[i] += length;
                }
            }
            Arrays.fill(counts, 0, classCount, 0);
            for (int index : shifted) {
                ++counts[classes[index]];
            }
            for (int i = 1; i < classCount; ++i) {
                counts[i] += counts[i - 1];
            }
            for (int i = length - 1; i >= 0; --i) {
                int index = shifted[i];
                order[--counts[classes[index]]] = index;
            }
            int nextCount = 1;
            nextClasses[order[0]] = 0;
            for (int i = 1; i < length; ++i) {
                int current = order[i];
                int previous = order[i - 1];
                int currentNext = current + shift;
                int previousNext = previous + shift;
                if (currentNext >= length) {
                    currentNext -= length;
                }
                if (previousNext >= length) {
                    previousNext -= length;
                }
                if (classes[current] != classes[previous]
                        || classes[currentNext] != classes[previousNext]) {
                    ++nextCount;
                }
                nextClasses[current] = nextCount - 1;
            }
            int[] temporary = classes;
            classes = nextClasses;
            nextClasses = temporary;
            classCount = nextCount;
        }
        return Arrays.copyOfRange(order, 1, length);
    }

    private static final class CommonPrefixes {
        private final int size;
        private final int[] ranks;
        private final int[] minimum;

        CommonPrefixes(String text) {
            size = text.length();
            int[] order = suffixArray(text);
            ranks = new int[size];
            minimum = new int[2 * size];
            Arrays.fill(minimum, size);
            for (int i = 0; i < size; ++i) {
                ranks[order[i]] = i;
            }
            int matched = 0;
            for (int i = 0; i < size; ++i) {
                int rank = ranks[i];
                if (rank + 1 == size) {
                    matched = 0;
                    continue;
                }
                int other = order[rank + 1];
                while (i + matched < size && other + matched < size
                        && text.charAt(i + matched) == text.charAt(other + matched)) {
                    ++matched;
                }
                minimum[size + rank] = matched;
                if (matched > 0) {
                    --matched;
                }
            }
            for (int i = size - 1; i > 0; --i) {
                minimum[i] = Math.min(minimum[2 * i], minimum[2 * i + 1]);
            }
        }

        int query(int first, int second) {
            int left = ranks[first];
            int right = ranks[second];
            if (left > right) {
                int temporary = left;
                left = right;
                right = temporary;
            }
            left += size;
            right += size;
            int result = size;
            while (left < right) {
                if (left % 2 == 1) {
                    result = Math.min(result, minimum[left++]);
                }
                if (right % 2 == 1) {
                    result = Math.min(result, minimum[--right]);
                }
                left /= 2;
                right /= 2;
            }
            return result;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int n = Integer.parseInt(nextToken(input));
        String text = nextToken(input);
        CommonPrefixes prefixes = new CommonPrefixes(text);
        int[][] representative = new int[ALPHABET_SIZE][ALPHABET_SIZE + 1];
        int[][] representativeCost = new int[ALPHABET_SIZE][ALPHABET_SIZE + 1];
        int[] representativeCount = new int[ALPHABET_SIZE];
        int[] farthest = new int[ALPHABET_SIZE + 1];
        int skipped = 0;
        for (int position = 0; position < n; ++position) {
            int letter = text.charAt(position) - FIRST_LETTER;
            int count = representativeCount[letter];
            int bestLength = 0;
            for (int index = count - 1; index >= 0; --index) {
                int previous = representative[letter][index];
                if (text.charAt(previous + bestLength) != text.charAt(position + bestLength)) {
                    continue;
                }
                int length = prefixes.query(previous, position);
                if (length > bestLength) {
                    int cost = representativeCost[letter][index];
                    farthest[cost] = Math.max(farthest[cost], position + length);
                    bestLength = length;
                    if (bestLength == n - position) {
                        break;
                    }
                }
            }
            // An earlier start with no larger cost dominates this start.
            if (count == 0 || skipped < representativeCost[letter][count - 1]) {
                representative[letter][count] = position;
                representativeCost[letter][count] = skipped;
                representativeCount[letter] = count + 1;
            }
            int nextCost = skipped + 1;
            for (int cost = 0; cost < nextCost; ++cost) {
                if (farthest[cost] >= position + 1) {
                    nextCost = cost;
                    break;
                }
            }
            skipped = nextCost;
        }
        System.out.print((n - skipped) + "\n");
    }
}
