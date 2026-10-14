import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int k = (int)in.nval;
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            nums[i] = (int)in.nval;
        }
        int height = (n + k - 1) / k; // the fewest rows that hold n numbers in k columns
        StringBuilder sb = new StringBuilder();
        for (int row = 0; row < height; row++) {
            // column c holds the numbers c * height ... c * height + height - 1
            for (int c = 0; c < k && c * height + row < n; c++)
                sb.append(String.format(Locale.US, "%4d", nums[c * height + row]));
            sb.append('\n');
        }
        System.out.print(sb);
    }
}
