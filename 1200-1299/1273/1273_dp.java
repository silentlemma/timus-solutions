import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int k = (int)in.nval;
        int[][] sleepers = new int[k][2];
        for (int[] s : sleepers) {
            in.nextToken();
            s[0] = (int)in.nval;
            in.nextToken();
            s[1] = (int)in.nval;
        }
        Arrays.sort(sleepers, (a, b) -> Integer.compare(a[0], b[0]));
        // two sleepers cross when their ends come in opposite orders, so the
        // kept ones form an increasing run of right ends
        int[] longest = new int[k];
        int best = 0;
        for (int i = 0; i < k; i++) {
            longest[i] = 1;
            for (int j = 0; j < i; j++)
                if (sleepers[j][1] < sleepers[i][1])
                    longest[i] = Math.max(longest[i], longest[j] + 1);
            best = Math.max(best, longest[i]);
        }
        System.out.println(k - best);
    }
}
