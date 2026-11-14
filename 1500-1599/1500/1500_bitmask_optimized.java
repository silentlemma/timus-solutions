import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int DECIMAL = 10;
    private static final int GROUP_BITS = 5;
    private static final int GROUPS = 4;
    private static final int GROUP_SIZE = 1 << GROUP_BITS;
    private static final int GROUP_MASK = GROUP_SIZE - 1;
    private static final int ROW_SIZE = GROUPS * GROUP_SIZE;
    private static final int HOME = 1;
    private static final int WORK = 2;

    private static int number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = input.read();
        }
        return value;
    }

    private static boolean connects(int[] roads, int permits) {
        int a = permits & GROUP_MASK;
        int b = GROUP_SIZE + ((permits >>> GROUP_BITS) & GROUP_MASK);
        int c = 2 * GROUP_SIZE + ((permits >>> (2 * GROUP_BITS)) & GROUP_MASK);
        int d = (GROUPS - 1) * GROUP_SIZE + (permits >>> ((GROUPS - 1) * GROUP_BITS));
        int seen = HOME;
        int pending = HOME;
        while (pending != 0) {
            int row = Integer.numberOfTrailingZeros(pending) * ROW_SIZE;
            pending &= pending - 1;
            int fresh = (roads[row + a] | roads[row + b] | roads[row + c] | roads[row + d]) & ~seen;
            if ((fresh & WORK) != 0) {
                return true;
            }
            seen |= fresh;
            pending |= fresh;
        }
        return false;
    }

    private static int choose(int[] roads, int required, int available, int count) {
        if (count == 0) {
            return connects(roads, required) ? required : -1;
        }
        while (Integer.bitCount(available) >= count) {
            int bit = Integer.lowestOneBit(available);
            available ^= bit;
            int answer = choose(roads, required | bit, available, count - 1);
            if (answer >= 0) {
                return answer;
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int categories = number(input), crossings = number(input), count = number(input);
        int[] roads = new int[crossings * ROW_SIZE];
        for (int i = 0; i < count; i++) {
            int a = number(input), b = number(input), category = number(input);
            int offset = category / GROUP_BITS * GROUP_SIZE + (1 << (category % GROUP_BITS));
            roads[a * ROW_SIZE + offset] |= 1 << b;
            roads[b * ROW_SIZE + offset] |= 1 << a;
        }
        for (int offset = 0; offset < roads.length; offset += GROUP_SIZE) {
            for (int mask = 1; mask < GROUP_SIZE; mask++) {
                int rest = mask & (mask - 1);
                roads[offset + mask] |= roads[offset + rest] | roads[offset + (mask ^ rest)];
            }
        }
        int all = (1 << categories) - 1;
        int required = 0;
        for (int category = 0; category < categories; category++) {
            int bit = 1 << category;
            if (!connects(roads, all ^ bit)) {
                required |= bit;
            }
        }
        int available = all ^ required;
        for (int extra = 0; extra <= Integer.bitCount(available); extra++) {
            int answer = choose(roads, required, available, extra);
            if (answer < 0) {
                continue;
            }
            StringBuilder output = new StringBuilder();
            output.append(Integer.bitCount(answer)).append('\n');
            String separator = "";
            while (answer != 0) {
                output.append(separator).append(Integer.numberOfTrailingZeros(answer));
                answer &= answer - 1;
                separator = " ";
            }
            System.out.println(output);
            return;
        }
    }
}
