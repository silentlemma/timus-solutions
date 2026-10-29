import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // the teacher's dates come sorted, so each of the student's dates is
        // looked up by binary search, counting repeats every time
        int[] known = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            known[i] = (int)in.nval;
        }
        in.nextToken();
        int m = (int)in.nval, count = 0;
        for (int i = 0; i < m; i++) {
            in.nextToken();
            if (Arrays.binarySearch(known, (int)in.nval) >= 0) {
                count++;
            }
        }
        System.out.println(count);
    }
}
