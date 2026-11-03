import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    static final int VALUE_BITS = 14, VALUE_MASK = (1 << VALUE_BITS) - 1;

    public static void main(String[] args) throws Exception {
        StreamTokenizer input = new StreamTokenizer(new InputStreamReader(System.in));
        input.nextToken();
        int n = (int)input.nval;
        int[] boxes = new int[n];
        for (int i = 0; i < n; i++) {
            input.nextToken();
            int count = (int)input.nval;
            input.nextToken();
            int first = (int)input.nval, previous = first;
            for (int j = 1; j < count; j++) {
                input.nextToken();
                int value = (int)input.nval;
                if (value < previous) {
                    System.out.println("NO");
                    return;
                }
                previous = value;
            }
            // Endpoints<=10000 fit14bits each; the28-bit key fits signed int32.
            boxes[i] = (first << VALUE_BITS) | previous;
        }
        Arrays.sort(boxes);
        int last = 0;
        for (int box : boxes) {
            if (last > (box >> VALUE_BITS)) {
                System.out.println("NO");
                return;
            }
            last = box & VALUE_MASK;
        }
        System.out.println("YES");
    }
}
