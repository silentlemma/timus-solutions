import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final int BUFFER_SIZE = 1 << 16;
    private static final int BYTE_MASK = 255;

    private static final class FastScanner {
        private final InputStream input;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        FastScanner(InputStream input) {
            this.input = input;
        }

        private int read() throws IOException {
            if (position == length) {
                length = input.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++] & BYTE_MASK;
        }

        int nextInt() throws IOException {
            int character;
            do {
                character = read();
            } while (character >= 0 && character <= ' ');
            int value = 0;
            while (character > ' ') {
                value = value * 10 + character - '0';
                character = read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        FastScanner input = new FastScanner(System.in);
        int suits = input.nextInt();
        int ranks = input.nextInt();
        int rows = input.nextInt();
        int total = suits * ranks;
        int[] left = new int[total];
        int[] degree = new int[total];
        Arrays.fill(left, -1);
        for (int card = 0; card < total; card++) {
            if (card % ranks != 0) {
                degree[card] = 1;
            }
        }
        for (int row = 0; row < rows; row++) {
            int size = input.nextInt();
            int previous = -1;
            for (int index = 0; index < size; index++) {
                int suit = input.nextInt() - 1;
                int rank = input.nextInt() - 1;
                int card = suit * ranks + rank;
                left[card] = previous;
                if (previous >= 0) {
                    degree[previous]++;
                }
                previous = card;
            }
        }

        int[] queue = new int[total];
        int head = 0;
        int tail = 0;
        for (int card = 0; card < total; card++) {
            if (degree[card] == 0) {
                queue[tail++] = card;
            }
        }
        while (head < tail) {
            int card = queue[head++];
            if (card % ranks + 1 < ranks) {
                int next = card + 1;
                if (--degree[next] == 0) {
                    queue[tail++] = next;
                }
            }
            int next = left[card];
            if (next >= 0 && --degree[next] == 0) {
                queue[tail++] = next;
            }
        }
        if (tail < total) {
            System.out.print("NO\n");
            return;
        }
        StringBuilder output = new StringBuilder("YES\n");
        for (int card : queue) {
            output.append(card / ranks + 1).append(' ').append(card % ranks + 1).append('\n');
        }
        System.out.print(output);
    }
}
