import java.io.IOException;
public class Main {

    static final int BUFFER_SIZE = 4096;
    static byte[] buffer = new byte[BUFFER_SIZE];
    static int position, length;
    // refillable storage bounds memory, not input length.
    static int read() throws IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length < 0)
                return -1;
        }
        return buffer[position++];
    }
    static int number() throws IOException {
        int c = read(), value = 0;
        while (c < '0' || c > '9')
            c = read();
        do {
            value = value * 10 + c - '0';
            c = read();
        } while (c >= '0' && c <= '9');
        return value;
    }

    static final int MAX_VALUE = 5000;
    public static void main(String[] args) throws IOException {
        int n = number();
        // counts can reach 100000, so a 16-bit frequency would overflow.
        int[] counts = new int[MAX_VALUE + 1];
        for (int i = 0; i < n; i++)
            counts[number()]++;
        for (int i = 1; i <= MAX_VALUE; i++)
            counts[i] += counts[i - 1];
        int k = number();
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < k; i++) {
            int rank = number(), low = 1, high = MAX_VALUE;
            while (low < high) {
                int mid = (low + high) / 2;
                if (counts[mid] < rank)
                    low = mid + 1;
                else
                    high = mid;
            }
            out.append(low).append('\n');
        }
        System.out.print(out);
    }
}
