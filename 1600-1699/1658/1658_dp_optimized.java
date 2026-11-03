import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static final int LONGEST = 100, TOP = 9, MAX_SUM = LONGEST * TOP, NONE = LONGEST + 1;
    static final int[] low = new int[MAX_SUM + 1], high = new int[MAX_SUM + 1];
    static final int[] offset = new int[MAX_SUM + 2];
    static byte[] fewest;

    static int lookup(int total, int squares) {
        if (total < 0 || total > MAX_SUM || squares < total || (squares - total) % 2 != 0)
            return NONE;
        int b = (squares - total) / 2;
        if (b < low[total] || b > high[total])
            return NONE;
        return fewest[offset[total] + b - low[total]];
    }

    public static void main(String[] args) throws Exception {
        for (int total = 0; total <= MAX_SUM; total++) {
            // Parity leaves b=(square_sum-total)/2. Balance 100 slots for
            // its minimum and pack nines for its maximum, bounding the row.
            int q = total / LONGEST, r = total % LONGEST;
            int least = (LONGEST - r) * q * q + r * (q + 1) * (q + 1);
            q = total / TOP;
            r = total % TOP;
            int greatest = q * TOP * TOP + r * r;
            low[total] = (least - total) / 2;
            high[total] = (greatest - total) / 2;
            offset[total + 1] = offset[total] + high[total] - low[total] + 1;
        }
        fewest = new byte[offset[MAX_SUM + 1]];
        Arrays.fill(fewest, (byte)NONE);
        fewest[0] = 0;
        for (int total = 1; total <= MAX_SUM; total++) {
            int destination = offset[total] - low[total];
            for (int digit = 1; digit <= Math.min(TOP, total); digit++) {
                int previous = total - digit, delta = digit * (digit - 1) / 2;
                int first = Math.max(low[total], low[previous] + delta);
                int last = Math.min(high[total], high[previous] + delta);
                int shift = offset[previous] - low[previous] - delta - destination;
                for (int position = destination + first; position <= destination + last;
                     position++) {
                    int value = fewest[position + shift] + 1;
                    if (value < fewest[position])
                        fewest[position] = (byte)value;
                }
            }
        }
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int tests = Integer.parseInt(input.readLine().trim());
        StringBuilder output = new StringBuilder();
        while (tests-- > 0) {
            StringTokenizer tokens = new StringTokenizer(input.readLine());
            int total = Integer.parseInt(tokens.nextToken());
            int squares = Integer.parseInt(tokens.nextToken());
            int size = lookup(total, squares);
            if (size == NONE) {
                output.append("No solution\n");
                continue;
            }
            int digit = 1;
            for (int left = size - 1; left >= 0; left--) {
                while (lookup(total - digit, squares - digit * digit) != left)
                    digit++;
                output.append((char)('0' + digit));
                total -= digit;
                squares -= digit * digit;
            }
            output.append('\n');
        }
        System.out.print(output);
    }
}
