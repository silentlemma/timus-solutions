import java.io.IOException;

public class Main {
    static final int MAX_WEIGHT = 130000;
    static final int BUFFER_SIZE = 4096;
    static final int BASE = 10;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int next, available;

    static int readByte() throws IOException {
        if (next >= available) {
            available = System.in.read(buffer);
            next = 0;
            if (available <= 0) {
                return -1;
            }
        }
        return buffer[next++];
    }

    static int readInt() throws IOException {
        int ch = readByte();
        while (ch >= 0 && ch <= ' ') {
            ch = readByte();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * BASE + ch - '0';
            ch = readByte();
        }
        return value;
    }

    static int gcd(int a, int b) {
        while (b != 0) {
            int remainder = a % b;
            a = b;
            b = remainder;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        int size = readInt();
        int[] positions = new int[MAX_WEIGHT + 1];
        int lightest = MAX_WEIGHT, heaviest = 0;
        for (int i = 1; i <= size; i++) {
            int weight = readInt();
            positions[weight] = i;
            lightest = Math.min(lightest, weight);
            heaviest = Math.max(heaviest, weight);
        }
        int rank = 0, ascending = 0, descending = 0;
        for (int weight = lightest; weight <= heaviest; weight++) {
            int position = positions[weight];
            if (position == 0) {
                continue;
            }
            rank++;
            ascending = gcd(ascending, Math.abs(position - rank));
            descending = gcd(descending, Math.abs(position - (size + 1 - rank)));
        }
        int step = ascending == 0 || descending == 0 ? size : Math.max(ascending, descending);
        System.out.println(step - 1);
    }
}
