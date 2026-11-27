import java.io.IOException;

public class Main {
    // the exponents p of the first 38 Mersenne primes 2^p - 1 (OEIS A000043)
    static final int[] EXPONENTS = {
        2,      3,      5,      7,       13,      17,      19,      31,      61,     89,
        107,    127,    521,    607,     1279,    2203,    2281,    3217,    4253,   4423,
        9689,   9941,   11213,  19937,   21701,   23209,   44497,   86243,   110503, 132049,
        216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593,
    };

    private static final int BUFFER_BYTES = 1024;
    private static final int BYTE_MASK = 255;
    private static final byte[] INPUT = new byte[BUFFER_BYTES];
    private static final byte[] OUTPUT = new byte[BUFFER_BYTES];
    private static final byte[] DIGITS = new byte[16];
    private static int inputPosition, inputLength, outputSize;

    private static int readByte() throws IOException {
        if (inputPosition == inputLength) {
            do {
                inputLength = System.in.read(INPUT);
            } while (inputLength == 0);
            inputPosition = 0;
            if (inputLength < 0) {
                inputLength = 0;
                return -1;
            }
        }
        return INPUT[inputPosition++] & BYTE_MASK;
    }

    private static int readInt() throws IOException {
        int ch = readByte();
        while (ch >= 0 && ch <= ' ')
            ch = readByte();
        if (ch == '+')
            ch = readByte();
        int value = 0;
        while (ch > ' ') {
            if (ch < '0' || ch > '9')
                throw new IOException("Invalid integer");
            value = value * 10 + ch - '0';
            ch = readByte();
        }
        return value;
    }

    private static void flushOutput() {
        System.out.write(OUTPUT, 0, outputSize);
        outputSize = 0;
    }

    private static void writeNumber(int value) {
        int first = DIGITS.length;
        do {
            DIGITS[--first] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        int length = DIGITS.length - first;
        if (outputSize + length + 1 > OUTPUT.length)
            flushOutput();
        System.arraycopy(DIGITS, first, OUTPUT, outputSize, length);
        outputSize += length;
        OUTPUT[outputSize++] = '\n';
    }

    public static void main(String[] args) throws IOException {
        int count = readInt();
        for (int index = 0; index < count; index++)
            writeNumber(EXPONENTS[readInt() - 1]);
        flushOutput();
        // Preserve complete output before skipping standalone JVM teardown.
        System.out.flush();
        System.err.flush();
        Runtime.getRuntime().halt(0);
    }
}
