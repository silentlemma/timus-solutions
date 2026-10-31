import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int l = (int)in.nval;
        in.nextToken();
        int k = (int)in.nval;
        in.nextToken();
        int h = (int)in.nval;
        // the time to reach x is x h / k plus a part that repeats every k km
        // and lies between 0 and h, so the last l mod k km take 0 to h hours
        int whole = l / k, slowest = whole + (l % k > 0 ? 1 : 0);
        // both bounds are integers <= 1000000; literal zeroes avoid floating formatting.
        System.out.println(whole * h + ".00000000 " + slowest * h + ".00000000");
    }
}
