import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    // Seven bits hold the start offset within a command of at most 100 letters.
    private static final int OFFSET_BITS = 7;
    private static final int OFFSET_MASK = (1 << OFFSET_BITS) - 1;

    private static int owner(int position) { return position >>> OFFSET_BITS; }

    private static int common(String a, int p, String b, int q) {
        int limit = Math.min(a.length() - p, b.length() - q);
        int length = 0;
        while (length < limit && a.charAt(p + length) == b.charAt(q + length)) {
            length++;
        }
        return length;
    }

    private static int compare(String[] words, int first, int second) {
        String a = words[owner(first)], b = words[owner(second)];
        int p = first & OFFSET_MASK, q = second & OFFSET_MASK;
        int length = common(a, p, b, q);
        if (p + length == a.length() || q + length == b.length()) {
            return (a.length() - p) - (b.length() - q);
        }
        return a.charAt(p + length) - b.charAt(q + length);
    }

    private static int[] sortedPositions(String[] words, int letters) {
        int[] positions = new int[letters];
        int[] buffer = new int[letters];
        int count = 0;
        for (int word = 0; word < words.length; word++) {
            for (int start = 0; start < words[word].length(); start++) {
                positions[count++] = (word << OFFSET_BITS) | start;
            }
        }
        // Merge primitive indices, with one shared scratch array for all passes.
        for (int width = 1; width < letters; width *= 2) {
            for (int start = 0; start < letters; start += 2 * width) {
                int middle = Math.min(start + width, letters);
                int end = Math.min(middle + width, letters);
                int left = start, right = middle;
                for (int at = start; at < end; at++) {
                    if (right == end ||
                        (left < middle && compare(words, positions[left], positions[right]) <= 0)) {
                        buffer[at] = positions[left++];
                    } else {
                        buffer[at] = positions[right++];
                    }
                }
            }
            int[] previous = positions;
            positions = buffer;
            buffer = previous;
        }
        return positions;
    }

    private static String[] shortestKeys(String[] words, int letters) {
        int[] positions = sortedPositions(words, letters);
        byte[] adjacent = new byte[letters];
        byte[] left = new byte[letters];
        int shared = 0;
        // The minimum adjacent LCP reaches the nearest suffix from another command.
        for (int i = 1; i < letters; i++) {
            int a = positions[i - 1], b = positions[i];
            int length = common(words[owner(a)], a & OFFSET_MASK, words[owner(b)], b & OFFSET_MASK);
            adjacent[i] = (byte)length;
            shared = owner(a) != owner(b) ? length : Math.min(shared, length);
            left[i] = (byte)shared;
        }
        int[] bestStart = new int[words.length];
        int[] bestLength = new int[words.length];
        for (int word = 0; word < words.length; word++) {
            bestLength[word] = words[word].length();
        }
        shared = 0;
        for (int i = letters - 1; i >= 0; i--) {
            int position = positions[i], word = owner(position), start = position & OFFSET_MASK;
            if (i + 1 < letters) {
                int length = adjacent[i + 1];
                shared = word != owner(positions[i + 1]) ? length : Math.min(shared, length);
            }
            int need = Math.max(shared, left[i]) + 1;
            if (need < bestLength[word] && start + need <= words[word].length()) {
                bestStart[word] = start;
                bestLength[word] = need;
            }
        }
        String[] keys = new String[words.length];
        for (int word = 0; word < words.length; word++) {
            keys[word] = words[word].substring(bestStart[word], bestStart[word] + bestLength[word]);
        }
        return keys;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.parseInt(input.readLine().trim());
        String[] words = new String[count];
        int letters = 0;
        for (int i = 0; i < count; i++) {
            words[i] = input.readLine().trim();
            letters += words[i].length();
        }
        for (String key : shortestKeys(words, letters)) {
            System.out.println(key);
        }
    }
}
