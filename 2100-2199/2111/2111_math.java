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
        long total = 0;
        for (int i = 0; i < n; i++) {
            in.nextToken();
            total += (long)in.nval;
        }
        // a trip to a city with load L costs L d there and (L - d) d back; summed over
        // any order this is (sum of d)^2, so the order does not matter
        System.out.println(total * total);
    }
}
