import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        StreamTokenizer input =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        input.nextToken();
        int size = (int)input.nval;
        input.nextToken();
        int limit = (int)input.nval, prefix = 0;
        // The total excess equals limit. A negative prefix makes the suffix
        // too heavy; a prefix above limit already violates the segment bound.
        for (int i = 0; i < size; i++) {
            input.nextToken();
            prefix += (int)input.nval - 1;
            if (prefix < 0 || prefix > limit) {
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }
}
