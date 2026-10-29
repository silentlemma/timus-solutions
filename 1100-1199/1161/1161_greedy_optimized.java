import java.util.Arrays;

public class Main {
    static final int DECIMAL_SCALE = 100;
    static final int MANTISSA_BITS = 52;
    static final int EXPONENT_BIAS = 1075;
    static final int BUFFER_SIZE = 4096;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, length;

    // the input is read in 4 KB blocks and the numbers are parsed by hand,
    // which needs much less memory than Scanner
    static int readByte() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length < 0)
                return -1;
        }
        return buffer[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c;
        do {
            c = readByte();
        } while (c >= 0 && c <= ' ');
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = readByte();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt();
        int[] weights = new int[n];
        for (int i = 0; i < n; i++)
            weights[i] = nextInt();
        Arrays.sort(weights);
        // each collision takes a square root of the product, so the heaviest
        // stripies should meet first and be rooted the most times
        double total = weights[n - 1];
        for (int i = n - 2; i >= 0; i--)
            total = 2 * Math.sqrt(total * weights[i]);
        // total is exactly mantissa / 2^shift; a merge never exceeds 2 * sqrt(x * 10000), so
        // total stays below 40000, shift is from 37 to 52, and 100 * mantissa < 100 * 2^53
        // still fits in a long
        long bits = Double.doubleToLongBits(total);
        int shift = EXPONENT_BIAS - (int)(bits >>> MANTISSA_BITS);
        long mantissa = (bits & ((1L << MANTISSA_BITS) - 1)) | (1L << MANTISSA_BITS);
        long scaled = mantissa * DECIMAL_SCALE;
        // hundredths rounded from the exact value, half to even, as printf in C
        long hundredths = scaled >> shift;
        long rest = scaled - (hundredths << shift);
        long half = 1L << (shift - 1);
        if (rest > half || rest == half && hundredths % 2 == 1)
            hundredths++;
        long fraction = hundredths % DECIMAL_SCALE;
        System.out.println(hundredths / DECIMAL_SCALE + "." + (fraction < 10 ? "0" : "") +
                           fraction);
    }
}
