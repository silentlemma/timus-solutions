import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int UPPER_COUNT = 26;
    private static final int BUFFER_SIZE = 1 << 16;

    private static class FastInput {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
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

        String next() throws IOException {
            StringBuilder token = new StringBuilder();
            int letter;
            do {
                letter = read();
            } while (letter >= 0 && letter <= ' ');
            while (letter > ' ') {
                token.append((char) letter);
                letter = read();
            }
            return token.toString();
        }
    }

    private static int symbolIndex(char letter) {
        return letter <= 'Z' ? letter - 'A' : letter - 'a' + UPPER_COUNT;
    }

    private static int solve(FastInput input) throws IOException {
        int k = Integer.parseInt(input.next());
        String message = input.next();
        String[] codes = new String[k];
        int singletons = 0;
        char good = '0';
        int capacity = 1;
        for (int symbol = 0; symbol < k; symbol++) {
            codes[symbol] = input.next();
            capacity += codes[symbol].length();
            if (codes[symbol].length() == 1) {
                singletons++;
                good = codes[symbol].charAt(0);
            }
        }
        if (singletons == 0) {
            int answer = 0;
            for (int position = 0; position < message.length(); position++) {
                answer += codes[symbolIndex(message.charAt(position))].length();
            }
            return answer;
        }
        if (singletons == 2) {
            return -1;
        }

        char bad = (char) ('0' + '1' - good);
        int[] weights = new int[k];
        char[][] reversed = new char[k][];
        int[][] next = new int[capacity][2];
        int[] fail = new int[capacity];
        boolean[] terminal = new boolean[capacity];
        int size = 1;
        for (int symbol = 0; symbol < k; symbol++) {
            String code = codes[symbol];
            reversed[symbol] = new char[code.length()];
            int state = 0;
            for (int position = code.length() - 1; position >= 0; position--) {
                char bit = code.charAt(position);
                reversed[symbol][code.length() - 1 - position] = bit;
                if (bit == bad) {
                    weights[symbol]++;
                }
                int edge = bit - '0';
                if (next[state][edge] == 0) {
                    next[state][edge] = size++;
                }
                state = next[state][edge];
            }
            terminal[state] = true;
        }
        int totalBad = 0;
        for (int position = 0; position < message.length(); position++) {
            totalBad += weights[symbolIndex(message.charAt(position))];
        }
        if (totalBad == 0) {
            return -1;
        }

        int[] queue = new int[size];
        int head = 0;
        int tail = 0;
        for (int bit = 0; bit < 2; bit++) {
            if (next[0][bit] != 0) {
                queue[tail++] = next[0][bit];
            }
        }
        while (head < tail) {
            int state = queue[head++];
            int fallback = fail[state];
            terminal[state] |= terminal[fallback];
            for (int bit = 0; bit < 2; bit++) {
                int child = next[state][bit];
                if (child == 0) {
                    next[state][bit] = next[fallback][bit];
                } else {
                    fail[child] = next[fallback][bit];
                    queue[tail++] = child;
                }
            }
        }

        // Cache complete codeword transitions instead of expanding the message.
        int[] cache = new int[size * k];
        int state = 0;
        int tailBad = 0;
        for (int position = message.length() - 1; position >= 0; position--) {
            int symbol = symbolIndex(message.charAt(position));
            int key = state * k + symbol;
            int edge = cache[key];
            if (edge == 0) {
                int target = state;
                int consumed = 0;
                for (char bit : reversed[symbol]) {
                    if (bit == bad) {
                        consumed++;
                    }
                    target = next[target][bit - '0'];
                    if (!terminal[target]) {
                        edge = -consumed;
                        break;
                    }
                }
                if (edge == 0) {
                    edge = target + 1;
                }
                cache[key] = edge;
            }
            if (edge < 0) {
                return totalBad - tailBad + edge + 1;
            }
            state = edge - 1;
            tailBad += weights[symbol];
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        System.out.println(solve(new FastInput()));
    }
}
