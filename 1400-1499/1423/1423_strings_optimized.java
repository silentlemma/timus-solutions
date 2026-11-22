public class Main {
    static final int BUFFER_SIZE = 4096, BYTE_MASK = 255;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0)
                return -1;
        }
        return buffer[position++] & BYTE_MASK;
    }
    static long nextLong() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = 10 * value + c - '0';
            c = read();
        }
        return value;
    }

    static byte[] token(int size) throws java.io.IOException {
        byte[] value = new byte[size];
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        for (int i = 0; i < size; i++) {
            value[i] = (byte)c;
            c = read();
        }
        return value;
    }
    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong();
        byte[] first = token(n), second = token(n);
        int[] failure = new int[n];
        for (int i = 1, k = 0; i < n; i++) {
            while (k > 0 && second[i] != second[k])
                k = failure[k - 1];
            if (second[i] == second[k])
                k++;
            failure[i] = k;
        }
        int cursor = 0;
        for (int i = 0, k = 0; i + 1 < 2 * n; i++) {
            byte c = first[cursor++];
            if (cursor == n)
                cursor = 0;
            while (k > 0 && c != second[k])
                k = failure[k - 1];
            if (c == second[k])
                k++;
            if (k == n) {
                int start = i - n + 1;
                System.out.println(start == 0 ? 0 : n - start);
                return;
            }
        }
        System.out.println(-1);
    }
}
