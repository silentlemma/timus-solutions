import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int MAX_PHONE = 100, MAX_WORD_LENGTH = 50, BUFFER_SIZE = 4096;
    static final String KEYPAD = "22233344115566070778889990";
    static final byte[] input = new byte[BUFFER_SIZE], token = new byte[MAX_PHONE + 1];
    static int position, available;

    static int read() throws IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static int next() throws IOException {
        int c = read(), length = 0;
        while (c >= 0 && c <= ' ')
            c = read();
        while (c > ' ') {
            token[length++] = (byte)c;
            c = read();
        }
        return length;
    }

    public static void main(String[] args) throws IOException {
        StringBuilder output = new StringBuilder();
        int n;
        while ((n = next()) > 0 && token[0] != '-') {
            byte[] phone = Arrays.copyOf(token, n);
            int count = 0, digits = next();
            for (int i = 0; i < digits; i++)
                count = count * 10 + token[i] - '0';
            int[] edges = new int[(n * MAX_WORD_LENGTH + 1) * 10];
            String[] words = new String[n * MAX_WORD_LENGTH + 1];
            int nodes = 1;
            // Build only substrings of the phone; a dictionary word cannot
            // allocate nodes. Reuse the token buffer for all discarded words.
            for (int start = 0; start < n; start++) {
                int node = 0;
                for (int end = start; end < Math.min(n, start + MAX_WORD_LENGTH); end++) {
                    int slot = node * 10 + phone[end] - '0';
                    if (edges[slot] == 0)
                        edges[slot] = nodes++;
                    node = edges[slot];
                }
            }
            for (int i = 0; i < count; i++) {
                int length = next(), node = 0;
                for (int j = 0; j < length; j++) {
                    node = edges[node * 10 + KEYPAD.charAt(token[j] - 'a') - '0'];
                    if (node == 0)
                        break;
                }
                if (node != 0 && words[node] == null)
                    words[node] = new String(token, 0, length, "US-ASCII");
            }
            int[] best = new int[n + 1], how = new int[n + 1];
            Arrays.fill(best, n + 1);
            best[0] = 0;
            for (int start = 0; start < n; start++) {
                if (best[start] > n)
                    continue;
                int node = 0;
                for (int end = start; end < Math.min(n, start + MAX_WORD_LENGTH); end++) {
                    node = edges[node * 10 + phone[end] - '0'];
                    if (words[node] != null && best[start] + 1 < best[end + 1]) {
                        best[end + 1] = best[start] + 1;
                        how[end + 1] = node;
                    }
                }
            }
            if (best[n] > n) {
                output.append("No solution.\n");
                continue;
            }
            String[] answer = new String[best[n]];
            for (int i = answer.length - 1, end = n; i >= 0; i--) {
                answer[i] = words[how[end]];
                end -= answer[i].length();
            }
            for (int i = 0; i < answer.length; i++) {
                if (i > 0)
                    output.append(' ');
                output.append(answer[i]);
            }
            output.append('\n');
        }
        System.out.print(output);
    }
}
