import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final long FIXED = 153; // 1 + 125 + 27: every multiple of 3 ends here
    static final long TEN = 10;
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer words = new StringTokenizer("");

    static long next() throws IOException {
        while (!words.hasMoreTokens())
            words = new StringTokenizer(in.readLine());
        return Long.parseLong(words.nextToken());
    }

    static long cubes(long x) {
        long s = 0;
        for (; x > 0; x /= TEN) {
            long d = x % TEN;
            s += d * d * d;
        }
        return s;
    }

    public static void main(String[] args) throws IOException {
        long t = next();
        StringBuilder out = new StringBuilder();
        for (long i = 0; i < t; i++) {
            long n = next(), gap = next(), l = next();
            // the gap before base N is F applied N - 1 times to K; from a
            // multiple of 3 it reaches 153 within 14 steps and stays there
            for (long step = 0; step < n - 1 && gap != FIXED; step++)
                gap = cubes(gap);
            out.append(gap - l).append('\n');
        }
        System.out.print(out);
    }
}
