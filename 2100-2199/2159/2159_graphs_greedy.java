import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.HashMap;
import java.util.PriorityQueue;

public class Main {
    private static final int BUFFER_SIZE = 1 << 16;
    private static final int INITIAL_TOKEN_CAPACITY = 32;
    private static final int NO_EDGE = -1;

    private static final class FastInput {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private char[] token = new char[INITIAL_TOKEN_CAPACITY];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = input.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int current;
            do {
                current = read();
            } while (current <= ' ');
            int value = 0;
            while (current > ' ') {
                value = value * 10 + current - '0';
                current = read();
            }
            return value;
        }

        String next() throws IOException {
            int current;
            do {
                current = read();
            } while (current <= ' ');
            int size = 0;
            while (current > ' ') {
                if (size == token.length) {
                    token = Arrays.copyOf(token, token.length * 2);
                }
                token[size++] = (char) current;
                current = read();
            }
            return new String(token, 0, size);
        }
    }

    private static final class Dictionary {
        final HashMap<String, Integer> ids;
        final String[] words;
        int size;

        Dictionary(int capacity) {
            ids = new HashMap<>(capacity * 2);
            words = new String[capacity];
        }

        int intern(String word) {
            Integer existing = ids.get(word);
            if (existing != null) {
                return existing;
            }
            int id = size++;
            ids.put(word, id);
            words[id] = word;
            return id;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int keywordCount = input.nextInt();
        int ruleCount = input.nextInt();
        int capacity = keywordCount + 2 * ruleCount;
        Dictionary dictionary = new Dictionary(capacity);
        for (int index = 0; index < keywordCount; ++index) {
            dictionary.intern(input.next());
        }

        int[] head = new int[capacity];
        Arrays.fill(head, NO_EDGE);
        int[] target = new int[ruleCount];
        int[] next = new int[ruleCount];
        for (int edge = 0; edge < ruleCount; ++edge) {
            int from = dictionary.intern(input.next());
            int to = dictionary.intern(input.next());
            target[edge] = to;
            next[edge] = head[from];
            head[from] = edge;
        }

        boolean[] required = new boolean[dictionary.size];
        int[] indegree = new int[dictionary.size];
        int[] queue = new int[dictionary.size];
        int requiredCount = keywordCount;
        for (int word = 0; word < keywordCount; ++word) {
            required[word] = true;
            queue[word] = word;
        }
        // Only edges leaving required words constrain the answer.
        for (int position = 0; position < requiredCount; ++position) {
            int word = queue[position];
            for (int edge = head[word]; edge != NO_EDGE; edge = next[edge]) {
                int to = target[edge];
                ++indegree[to];
                if (!required[to]) {
                    required[to] = true;
                    queue[requiredCount++] = to;
                }
            }
        }

        PriorityQueue<Integer> ready = new PriorityQueue<>(
                (left, right) -> dictionary.words[left].compareTo(dictionary.words[right]));
        for (int position = 0; position < requiredCount; ++position) {
            int word = queue[position];
            if (indegree[word] == 0) {
                ready.add(word);
            }
        }

        StringBuilder answer = new StringBuilder();
        int emitted = 0;
        while (!ready.isEmpty()) {
            int word = ready.remove();
            if (emitted > 0) {
                answer.append(' ');
            }
            answer.append(dictionary.words[word]);
            ++emitted;
            for (int edge = head[word]; edge != NO_EDGE; edge = next[edge]) {
                int to = target[edge];
                if (--indegree[to] == 0) {
                    ready.add(to);
                }
            }
        }

        if (emitted != requiredCount) {
            System.out.print("-1\n");
        } else {
            answer.append('\n');
            System.out.print(answer);
        }
    }
}
