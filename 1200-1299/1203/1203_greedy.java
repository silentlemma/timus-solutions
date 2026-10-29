import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int TIME = 30000;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // the latest start among the talks that end at each minute
        int[] latest = new int[TIME + 1];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            int s = (int)in.nval;
            in.nextToken();
            int e = (int)in.nval;
            latest[e] = Math.max(latest[e], s);
        }
        // take the talk that ends first among those starting after the last one
        int count = 0, last = 0;
        for (int e = 1; e <= TIME; e++) {
            if (latest[e] > last) {
                count++;
                last = e;
            }
        }
        System.out.println(count);
    }
}
