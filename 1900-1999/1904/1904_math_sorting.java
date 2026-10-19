import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    private static final class Interval {
        final int left;
        int right;

        Interval(int left, int right) {
            this.left = left;
            this.right = right;
        }
    }

    private static final class Input {
        private final BufferedInputStream stream = new BufferedInputStream(System.in);

        int next() throws IOException {
            int c;
            do {
                c = stream.read();
            } while (c <= ' ' && c >= 0);
            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = stream.read();
            }
            int value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = stream.read();
            }
            return sign * value;
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int count = input.next();
        int[] constants = new int[count];
        for (int i = 0; i < count; i++) {
            constants[i] = input.next();
        }
        List<Interval> intervals = new ArrayList<>();
        intervals.add(new Interval(0, 1));
        for (int i = count - 1; i >= 0; i--) {
            List<Interval> candidates = new ArrayList<>();
            for (Interval item : intervals) {
                if (item.right < 0) {
                    continue;
                }
                int left = Math.max(item.left, 0);
                candidates.add(new Interval(constants[i] - item.right, constants[i] - left));
                candidates.add(new Interval(constants[i] + left, constants[i] + item.right));
            }
            candidates.sort((a, b) -> a.left != b.left
                ? Integer.compare(a.left, b.left) : Integer.compare(a.right, b.right));
            List<Interval> merged = new ArrayList<>();
            for (Interval item : candidates) {
                if (!merged.isEmpty() && item.left <= merged.get(merged.size() - 1).right) {
                    Interval last = merged.get(merged.size() - 1);
                    last.right = Math.max(last.right, item.right);
                } else {
                    merged.add(item);
                }
            }
            intervals = merged;
        }
        StringBuilder output = new StringBuilder();
        output.append(intervals.size()).append('\n');
        for (Interval item : intervals) {
            output.append(item.left).append(' ').append(item.right).append('\n');
        }
        System.out.print(output);
    }
}
