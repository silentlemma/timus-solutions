import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int LARGEST = 25000;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
            new BufferedReader(new InputStreamReader(new BufferedInputStream(System.in))));
        in.nextToken();
        int n = (int)in.nval;
        // counting each value is a sort in descending order, and printing the
        // conjugate partition twice gives back the sorted array
        int[] count = new int[LARGEST + 1];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            count[(int)in.nval]++;
        }
        StringBuilder out = new StringBuilder();
        for (int value = LARGEST; value >= 1; value--) {
            for (int k = 0; k < count[value]; k++)
                out.append(value).append('\n');
        }
        System.out.print(out);
    }
}
