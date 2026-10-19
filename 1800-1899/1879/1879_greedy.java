import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int LETTERS = 100000;
    static StreamTokenizer in;

    static int nextInt() throws IOException {
        in.nextToken();
        return (int) in.nval;
    }

    static long[] readCounts(int length) throws IOException {
        long[] count = new long[LETTERS + 1];
        for (int i = 0; i < length; i++) {
            count[nextInt()]++;
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        long n = nextInt();
        long[] a = readCounts((int) n);
        long m = nextInt();
        long[] b = readCounts((int) m);
        // every position of t meets every position of the cyclic s exactly once,
        // so the distance is n m minus the number of equal pairs
        long p = a[0];
        long q = b[0];
        long equal = 0;
        long same = 0;
        long maxA = 0;
        long maxB = 0;
        for (int c = 1; c <= LETTERS; c++) {
            equal += a[c] * b[c];
            same = Math.max(same, p * b[c] + q * a[c]);
            maxA = Math.max(maxA, a[c]);
            maxB = Math.max(maxB, b[c]);
        }
        // the gain is linear in the letters chosen for the question marks of one
        // string, so all of them take one letter: the same letter for both
        // strings, or the best letter for each
        same += p * q;
        long best = Math.max(same, p * maxB + q * maxA);
        System.out.println(n * m - equal - best);
    }
}
