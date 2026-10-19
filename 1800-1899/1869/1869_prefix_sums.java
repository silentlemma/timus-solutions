import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int SEATS = 36;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int) in.nval;
        // change[k] is how many people get on at station k minus how many get
        // off there; the eastbound and westbound trains are counted apart
        long[] east = new long[n + 1];
        long[] west = new long[n + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                in.nextToken();
                long a = (long) in.nval;
                if (i < j) {
                    east[i] += a;
                    east[j] -= a;
                } else if (i > j) {
                    west[j] += a;
                    west[i] -= a;
                }
            }
        }
        long best = 0;
        long loadE = 0;
        long loadW = 0;
        for (int k = 0; k < n; k++) {
            loadE += east[k];
            loadW += west[k];
            best = Math.max(best, Math.max(loadE, loadW));
        }
        System.out.println((best + SEATS - 1) / SEATS);
    }
}
