import java.io.IOException;

public class Main {
    // sieving this range gives 15000 primes, enough for every statement query.
    private static final int LIMIT = 163842;
    private static final int PRIME_COUNT = 15000;
    private static final int FIRST_ODD_PRIME = 3;
    // refillable chunks handle any input length without retaining the whole input.
    private static final int BUFFER_SIZE = 8192;
    private static final byte[] input = new byte[BUFFER_SIZE];
    private static int position, length;

    private static int readByte() throws IOException {
        if (position == length) {
            length = System.in.read(input);
            position = 0;
            if (length < 0)
                return -1;
        }
        return input[position++];
    }

    // parse positive decimal tokens directly to avoid scanner allocations.
    private static int nextInt() throws IOException {
        int c;
        do {
            c = readByte();
        } while (c <= ' ' && c != -1);
        int value = 0;
        while (c > ' ') {
            value = value * 10 + c - '0';
            c = readByte();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        // index i represents 2*i+1; skip even numbers and store only 15000 primes.
        boolean[] composite = new boolean[LIMIT / 2];
        for (int p = FIRST_ODD_PRIME; p * p < LIMIT; p += 2) {
            if (!composite[p / 2]) {
                for (int i = p * p / 2; i < composite.length; i += p) {
                    composite[i] = true;
                }
            }
        }
        int[] primes = new int[PRIME_COUNT];
        primes[0] = 2;
        int primeCount = 1;
        for (int p = FIRST_ODD_PRIME; p < LIMIT; p += 2) {
            if (!composite[p / 2])
                primes[primeCount++] = p;
        }
        int queries = nextInt();
        byte[] output = new byte[BUFFER_SIZE];
        // every output is a positive int, so ten decimal digits suffice.
        final int MAX_DIGITS = 10;
        byte[] digits = new byte[MAX_DIGITS];
        int used = 0;
        for (int k = 0; k < queries; k++) {
            int value = primes[nextInt() - 1], count = 0;
            do {
                digits[count++] = (byte)('0' + value % 10);
                value /= 10;
            } while (value != 0);
            if (used + count + 1 > output.length) {
                System.out.write(output, 0, used);
                used = 0;
            }
            while (count > 0)
                output[used++] = digits[--count];
            output[used++] = (byte)'\n';
        }
        System.out.write(output, 0, used);
        System.out.flush();
    }
}
