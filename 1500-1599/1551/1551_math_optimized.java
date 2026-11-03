import java.util.HashMap;
import java.util.Map;

public class Main {
    static final int MAX_NAME = 30;
    static final char[] token = new char[MAX_NAME];
    static final int BUFFER_SIZE = 4096;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    static void skipName() throws java.io.IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        while (c > ' ')
            c = read();
    }

    static String prefecture() throws java.io.IOException {
        int c = read(), length = 0;
        while (c <= ' ')
            c = read();
        while (c > ' ') {
            token[length++] = (char)c;
            c = read();
        }
        return new String(token, 0, length);
    }

    public static void main(String[] args) throws Exception {
        int n = nextInt(), largest = 0;
        Map<String, Integer> counts = new HashMap<>();
        for (int i = 0; i < (1 << n); i++) {
            skipName();
            String prefecture = prefecture();
            Integer previous = counts.get(prefecture);
            int count = previous == null ? 1 : previous + 1;
            counts.put(prefecture, count);
            if (count > largest)
                largest = count;
        }
        int unsafe = Integer.SIZE - Integer.numberOfLeadingZeros(largest - 1);
        System.out.println(n - unsafe);
    }
}
