import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    private static final long MIN_SUM = 3;

    private static long longestChain(long first, long second) {
        if (first > second) {
            long temporary = first;
            first = second;
            second = temporary;
        }
        long difference = second - first;
        if (difference == 0) {
            return 2;
        }
        if (difference == 1) {
            return second - 1;
        }
        if (difference == 2) {
            if (second % 2 == 1) {
                return second - 1;
            }
            return second / 2;
        }
        // A longest chain joins two distinct residue classes modulo the difference.
        return 2 * ((second - MIN_SUM) / difference + 1);
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer input = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));
        input.nextToken();
        long first = (long) input.nval;
        input.nextToken();
        long second = (long) input.nval;
        System.out.println(longestChain(first, second));
    }
}
