import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int) in.nval;
        int[] w = new int[n];
        int total = 0;
        for (int i = 0; i < n; i++) {
            in.nextToken();
            w[i] = (int) in.nval;
            total += w[i];
        }
        // reach[s]: some stones weigh exactly s; the lighter pile is at most total/2
        int half = total / 2;
        boolean[] reach = new boolean[half + 1];
        reach[0] = true;
        for (int x : w) {
            for (int s = half; s >= x; s--) {
                if (reach[s - x]) {
                    reach[s] = true;
                }
            }
        }
        int s = half;
        while (!reach[s]) {
            s--;
        }
        System.out.println(total - 2 * s);
    }
}
