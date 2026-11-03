public class Main {
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

    static final byte[] output = new byte[BUFFER_SIZE];
    static int used;

    static void write(int c) throws java.io.IOException {
        if (used == BUFFER_SIZE) {
            System.out.write(output, 0, used);
            used = 0;
        }
        output[used++] = (byte)c;
    }

    static void writeInt(int value, byte[] digits) throws java.io.IOException {
        int count = 0;
        do {
            digits[count++] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        while (count != 0)
            write(digits[--count]);
    }

    public static void main(String[] args) throws Exception {
        int n = nextInt();
        // At most(n+1)*10000<=1000010000 coins: signed32-bit cells suffice.
        int[] diff = new int[n + 2];
        for (int i = 0; i <= n; i++) {
            int a = nextInt(), b = nextInt(), amount = nextInt();
            diff[a] += amount;
            diff[b + 1] -= amount;
        }
        int total = 0;
        byte[] digits = new byte[10];
        for (int i = 1; i <= n; i++) {
            total += diff[i];
            writeInt(total, digits);
            write(i < n ? ' ' : '\n');
        }
        System.out.write(output, 0, used);
    }
}
