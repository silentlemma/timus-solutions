import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // best is the largest segment sum so far (the empty segment gives 0), and
        // ending is the largest sum of a segment that ends at the current number
        long best = 0, ending = 0;
        for (int i = 0; i < n; i++) {
            in.nextToken();
            ending = Math.max(ending + (long)in.nval, 0);
            best = Math.max(best, ending);
        }
        System.out.println(best);
    }
}
