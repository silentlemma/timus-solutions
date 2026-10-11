import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static StreamTokenizer in =
        new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    static long next() throws IOException {
        in.nextToken();
        return (long)in.nval;
    }

    public static void main(String[] args) throws IOException {
        int layers = (int)next();
        // the layer above, each brick with all it carries, as its ends, the weight
        // (lengths) and twice its moment about 0, R^2 - L^2 per brick
        long[] aLeft = new long[0], aRight = new long[0], aWeight = new long[0],
               aMoment = new long[0];
        for (int layer = 0; layer < layers; layer++) {
            int k = (int)next();
            long[] left = new long[k], right = new long[k], weight = new long[k],
                   moment = new long[k];
            for (int i = 0; i < k; i++) {
                left[i] = next();
                right[i] = next();
                weight[i] = right[i] - left[i];
                moment[i] = right[i] * right[i] - left[i] * left[i];
            }
            // each brick above rests on the one brick below that it overlaps, and
            // the centre of all it carries must lie strictly inside the overlap, a test
            // that the doubled moment keeps in whole numbers
            int j = 0;
            for (int a = 0; a < aLeft.length; a++) {
                while (j < k && right[j] <= aLeft[a])
                    j++;
                if (j == k || left[j] >= aRight[a]) {
                    System.out.println("No");
                    return;
                }
                long lo = Math.max(aLeft[a], left[j]), hi = Math.min(aRight[a], right[j]);
                if (!(2 * lo * aWeight[a] < aMoment[a] && aMoment[a] < 2 * hi * aWeight[a])) {
                    System.out.println("No");
                    return;
                }
                weight[j] += aWeight[a];
                moment[j] += aMoment[a];
            }
            aLeft = left;
            aRight = right;
            aWeight = weight;
            aMoment = moment;
        }
        System.out.println("Yes");
    }
}
