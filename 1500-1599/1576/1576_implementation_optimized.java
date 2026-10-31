public class Main {

    // refill a small buffer instead of retaining the input or allocating tokens.
    static final int BUFFER_SIZE = 4096;
    static final byte[] BUFFER = new byte[BUFFER_SIZE];
    static int position, length;
    static int read() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(BUFFER);
            position = 0;
            if (length < 0)
                return -1;
        }
        return BUFFER[position++];
    }
    static int nextInt() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value * sign;
    }

    static final int FREE = 6; // calls of up to six seconds cost nothing
    static final int MINUTE = 60;

    public static void main(String[] args) throws java.io.IOException {
        long n1 = nextInt(), c1 = nextInt();
        long n2 = nextInt(), t = nextInt(), c2 = nextInt();
        long n3 = nextInt();
        int k = nextInt();
        long minutes = 0;
        for (int i = 0; i < k; i++) {
            int seconds = nextInt() * MINUTE + nextInt();
            if (seconds > FREE)
                minutes += (seconds + MINUTE - 1) / MINUTE; // a started minute counts in full
        }
        System.out.println("Basic:     " + (n1 + c1 * minutes));
        System.out.println("Combined:  " + (n2 + c2 * Math.max(0, minutes - t)));
        System.out.println("Unlimited: " + n3);
    }
}
