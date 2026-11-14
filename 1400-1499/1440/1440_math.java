import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    private static final List<String> DAYS =
        Arrays.asList("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday");
    private static final List<String> MONTHS =
        Arrays.asList("September", "October", "November", "December");
    // Days elapsed since September 1.
    private static final int[] OFFSETS = {0, 30, 61, 91};

    private static class Input {
        final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer words = new StringTokenizer("");

        String next() throws IOException {
            while (!words.hasMoreTokens()) {
                words = new StringTokenizer(reader.readLine());
            }
            return words.nextToken();
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int start = DAYS.indexOf(input.next()) + 1;
        int month = MONTHS.indexOf(input.next());
        int day = Integer.parseInt(input.next());
        int minimum = Integer.parseInt(input.next()), maximum = Integer.parseInt(input.next());
        int week = DAYS.size(), training = OFFSETS[month] + day - 2;
        int regular = training / week, extra = training % week;
        // The first extra weekdays occur once more than the others.
        for (int count = 1; count <= week; ++count) {
            int low = Math.max(0, Math.max(count - (week - extra), minimum - count * regular));
            int high = Math.min(count, Math.min(extra, maximum - count * regular));
            if (low <= high) {
                StringBuilder output = new StringBuilder().append(count).append('\n');
                for (int i = 0; i < low; ++i) {
                    output.append(DAYS.get((start + i) % week)).append('\n');
                }
                for (int i = 0; i < count - low; ++i) {
                    output.append(DAYS.get((start + extra + i) % week)).append('\n');
                }
                System.out.print(output);
                return;
            }
        }
        System.out.println("Impossible");
    }
}
