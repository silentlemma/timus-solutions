import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {
    static final int TWO = 2;
    static final int THREE = 3;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.parseNumbers();
        if (in.nextToken() == StreamTokenizer.TT_EOF)
            return;
        int n = (int)in.nval;
        int[] marks = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            marks[i] = (int)in.nval;
        }
        // a nonzero product is +-2^a 3^b: prefix counts of twos and threes
        int[] twos = new int[n + 1], threes = new int[n + 1];
        boolean zero = false;
        for (int i = 0; i < n; i++) {
            twos[i + 1] = twos[i] + (Math.abs(marks[i]) == TWO ? 1 : 0);
            threes[i + 1] = threes[i] + (Math.abs(marks[i]) == THREE ? 1 : 0);
            zero = zero || marks[i] == 0;
        }
        double logTwo = Math.log(TWO), logThree = Math.log(THREE);
        boolean found = false; // the exponents of the best positive product
        int bestA = 0, bestB = 0;
        int i = 0;
        while (i < n) {
            if (marks[i] == 0) {
                i++;
                continue;
            }
            // a run without zeros: |x| >= 1, so longer runs never shrink the size
            int j = i;
            List<Integer> negatives = new ArrayList<>();
            while (j < n && marks[j] != 0) {
                if (marks[j] < 0)
                    negatives.add(j);
                j++;
            }
            int[][] spans;
            if (negatives.size() % 2 == 0) {
                spans = new int[][] {{i, j}};
            } else {
                // drop the part up to the first negative or from the last one
                spans = new int[][] {{negatives.get(0) + 1, j},
                                     {i, negatives.get(negatives.size() - 1)}};
            }
            for (int[] s : spans) {
                int lo = s[0], hi = s[1];
                if (lo >= hi)
                    continue;
                int a = twos[hi] - twos[lo], b = threes[hi] - threes[lo];
                if (!found || a * logTwo + b * logThree > bestA * logTwo + bestB * logThree) {
                    found = true;
                    bestA = a;
                    bestB = b;
                }
            }
            i = j;
        }
        if (!found) {
            // all marks are zeros or lone negatives
            System.out.println(zero ? 0 : marks[0]);
            return;
        }
        BigInteger p =
            BigInteger.valueOf(TWO).pow(bestA).multiply(BigInteger.valueOf(THREE).pow(bestB));
        System.out.println(p.toString());
    }
}
