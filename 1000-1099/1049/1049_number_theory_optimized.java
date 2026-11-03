public class Main {
    static final int COUNT = 10, BASE = 10, MAX_VALUE = 10000;
    // Six distinct prime factors require at least2*3*5*7*11*13>10000.
    static final int MAX_DISTINCT_PER_VALUE = 5;
    static final char[] exponent = new char[MAX_VALUE + 1];
    static final int[] touched = new int[COUNT * MAX_DISTINCT_PER_VALUE];
    static int used;
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

    static void addPrime(int prime, int power) {
        if (exponent[prime] == 0)
            touched[used++] = prime;
        // The largest exponent is10*floor(log2(10000))=130: char is safe.
        exponent[prime] += power;
    }

    public static void main(String[] args) throws Exception {
        for (int i = 0; i < COUNT; i++) {
            int value = nextInt();
            for (int prime = 2; prime * prime <= value; prime += prime == 2 ? 1 : 2) {
                int power = 0;
                while (value % prime == 0) {
                    power++;
                    value /= prime;
                }
                if (power > 0)
                    addPrime(prime, power);
            }
            if (value > 1)
                addPrime(value, 1);
        }
        int answer = 1;
        for (int i = 0; i < used; i++)
            answer = answer * (exponent[touched[i]] + 1) % BASE;
        System.out.println(answer);
    }
}
