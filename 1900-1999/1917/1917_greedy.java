import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[] safeRemovals(int[] input, long budget) {
        int[] values = input.clone();
        Arrays.sort(values);
        int removed = 0;
        int spells = 0;
        int active = 0;
        for (int start = 0; start < values.length;) {
            int end = start + 1;
            while (end < values.length && values[end] == values[start]) {
                end++;
            }
            int count = end - start;
            long threshold = values[start];
            if (count * threshold > budget) {
                break;
            }
            if ((active + count) * threshold > budget) {
                spells++;
                active = 0;
            }
            active += count;
            removed += count;
            start = end;
        }
        return new int[] {removed, spells + (active > 0 ? 1 : 0)};
    }

    private static final class Input {
        final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokens = new StringTokenizer("");

        int next() throws IOException {
            while (!tokens.hasMoreTokens()) {
                tokens = new StringTokenizer(reader.readLine());
            }
            return Integer.parseInt(tokens.nextToken());
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int count = input.next();
        long budget = input.next();
        int[] values = new int[count];
        for (int index = 0; index < count; index++) {
            values[index] = input.next();
        }
        int[] answer = safeRemovals(values, budget);
        System.out.println(answer[0] + " " + answer[1]);
    }
}
