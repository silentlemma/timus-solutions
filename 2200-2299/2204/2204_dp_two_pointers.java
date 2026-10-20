import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int OPTIONS = 2;
    private static final int BUFFER_SIZE = 65536;

    private static final class FastScanner {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = input.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int character = read();
            while (character <= ' ') {
                character = read();
            }
            int value = 0;
            while (character >= '0' && character <= '9') {
                value = value * 10 + character - '0';
                character = read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        FastScanner input = new FastScanner();
        int examCount = input.nextInt();
        int tripCount = input.nextInt();
        int alternativeCount = OPTIONS * examCount;
        int[] examLeft = new int[alternativeCount];
        int[] examRight = new int[alternativeCount];
        for (int interval = 0; interval < alternativeCount; interval++) {
            examLeft[interval] = input.nextInt();
            examRight[interval] = input.nextInt();
        }
        int[] tripLeft = new int[tripCount];
        int[] tripRight = new int[tripCount];
        for (int trip = 0; trip < tripCount; trip++) {
            tripLeft[trip] = input.nextInt();
            tripRight[trip] = input.nextInt();
        }

        int[] previousFirst = new int[OPTIONS];
        int[] previousEnd = new int[OPTIONS];
        int[] previousCost = new int[OPTIONS];
        int[] currentFirst = new int[OPTIONS];
        int[] currentEnd = new int[OPTIONS];
        int[] currentCost = new int[OPTIONS];
        int first = 0;
        int end = 0;
        for (int exam = 0; exam < examCount; exam++) {
            for (int option = 0; option < OPTIONS; option++) {
                int interval = OPTIONS * exam + option;
                while (first < tripCount && tripRight[first] < examLeft[interval]) {
                    first++;
                }
                while (end < tripCount && tripLeft[end] <= examRight[interval]) {
                    end++;
                }
                currentFirst[option] = first;
                currentEnd[option] = end;
                int best = tripCount + 1;
                for (int previous = 0; previous < OPTIONS; previous++) {
                    // Only one trip can intersect two separated exam intervals.
                    boolean shared = first < end
                            && previousFirst[previous] < previousEnd[previous]
                            && previousEnd[previous] - 1 == first;
                    int cost = previousCost[previous] - (shared ? 1 : 0);
                    best = Math.min(best, cost);
                }
                currentCost[option] = end - first + best;
            }
            int[] temporary = previousFirst;
            previousFirst = currentFirst;
            currentFirst = temporary;
            temporary = previousEnd;
            previousEnd = currentEnd;
            currentEnd = temporary;
            temporary = previousCost;
            previousCost = currentCost;
            currentCost = temporary;
        }
        System.out.println(tripCount - Math.min(previousCost[0], previousCost[1]));
    }
}
