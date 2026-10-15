import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static int[] diff;
    static int last;
    static StreamTokenizer in;

    static int next() throws IOException {
        in.nextToken();
        return (int) in.nval;
    }

    static void add(int lo, int hi, int value) {
        lo = Math.max(lo, 0);
        hi = Math.min(hi, last);
        if (lo <= hi) {
            diff[lo] += value;
            diff[hi + 1] -= value;
        }
    }

    public static void main(String[] args) throws IOException {
        in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int g = next();
        int w = next();
        int b = next();
        int p = next();
        int n = next();
        last = g - b; // the barbell starts at s = 0 .. g - b
        diff = new int[last + 2];
        for (int i = 0; i < n; i++) {
            int x = next();
            // a plate [a, a + p] hurts the worm [x, x + w] when they overlap by a
            // positive length, that is for whole a from x - p + 1 to x + w - 1.
            // The left plate starts at s, the right one at s + b - p
            int lo1 = x - p + 1;
            int hi1 = x + w - 1;
            int lo2 = x - b + 1;
            int hi2 = x + w - 1 - b + p;
            add(lo1, hi1, 1);
            add(lo2, hi2, 1);
            // a worm under both plates is hurt once
            add(Math.max(lo1, lo2), Math.min(hi1, hi2), -1);
        }
        int best = 0;
        int bestHurt = 0;
        int hurt = 0;
        for (int s = 0; s <= last; s++) {
            hurt += diff[s];
            if (s == 0 || hurt < bestHurt) {
                bestHurt = hurt;
                best = s;
            }
        }
        System.out.println(best);
    }
}
