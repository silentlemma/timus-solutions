import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int HOURS = 12;
    private static final int MINUTE = 60;
    private static final int HOUR = MINUTE * MINUTE;
    private static final int DIAL = HOURS * HOUR;

    private static int number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && (c <= ' ' || c == ':')) {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = input.read();
        }
        return value;
    }

    private static int choose(char[] frequency, int count) {
        int later = count;
        long bestCost = (long)count * DIAL;
        int bestTime = 0;
        for (int target = 0; target < DIAL; target++) {
            int clocks = frequency[target];
            if (clocks == 0) {
                continue;
            }
            later -= clocks;
            long cost = (long)count * target + (long)DIAL * later;
            if (cost < bestCost) {
                bestCost = cost;
                bestTime = target;
            }
        }
        return bestTime;
    }

    private static void appendTwoDigits(StringBuilder output, int value) {
        output.append((char)('0' + value / 10));
        output.append((char)('0' + value % 10));
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int count = number(input);
        char[] frequency = new char[DIAL];
        for (int i = 0; i < count; i++) {
            int h = number(input), m = number(input), s = number(input);
            frequency[h % HOURS * HOUR + m * MINUTE + s]++;
        }
        int target = choose(frequency, count);
        int h = target / HOUR;
        StringBuilder output = new StringBuilder();
        output.append(h == 0 ? HOURS : h).append(':');
        appendTwoDigits(output, target / MINUTE % MINUTE);
        output.append(':');
        appendTwoDigits(output, target % MINUTE);
        System.out.println(output);
    }
}
