public class Main {
    private static final int INPUT_BUFFER_SIZE = 4096;
    private static final byte[] input = new byte[INPUT_BUFFER_SIZE];
    private static int position;
    private static int length;

    private static int readByte() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(input);
            position = 0;
            if (length < 0) {
                return -1;
            }
        }
        return input[position++];
    }

    private static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = readByte();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = readByte();
        }
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = readByte();
        }
        return value * sign;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong();
        long total = 0;
        for (int i = 0; i < n; i++) {
            total += nextLong();
        }
        // a trip to a city with load L costs L d there and (L - d) d back; summed over
        // any order this is (sum of d)^2, so the order does not matter
        System.out.println(total * total);
    }
}
