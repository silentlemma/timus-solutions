import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    // the exponents p of the first 38 Mersenne primes 2^p - 1, in increasing order
    static final int[] EXPONENTS = {
        2,      3,      5,      7,       13,      17,      19,      31,      61,     89,
        107,    127,    521,    607,     1279,    2203,    2281,    3217,    4253,   4423,
        9689,   9941,   11213,  19937,   21701,   23209,   44497,   86243,   110503, 132049,
        216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593,
    };

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int count = (int)in.nval;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < count; i++) {
            in.nextToken();
            out.append(EXPONENTS[(int)in.nval - 1]).append('\n');
        }
        System.out.print(out);
    }
}
