import java.util.*;

public class Main {
    static final int DIGITS = 10;
    static final long PAIR = DIGITS * (DIGITS - 1); // two free mirrored digits that differ

    // lucky numbers of this length that start with these digits
    static long complete(int[] prefix, int fixed, int length) {
        long ways = 1;
        for (int i = 0; i < (length + 1) / 2; i++) {
            int j = length - 1 - i;
            if (i == j)
                ways *= i < fixed ? 1 : DIGITS;
            else if (j < fixed) {
                if (prefix[i] == prefix[j])
                    return 0;
            } else if (i < fixed)
                ways *= DIGITS - 1; // the partner must differ from the fixed digit
            else
                ways *= PAIR;
        }
        return ways;
    }

    // lucky tickets numbered 1 .. n
    static long luckyUpTo(long n) {
        if (n <= 0)
            return 0;
        String s = Long.toString(n);
        int length = s.length();
        int[] digits = new int[length];
        for (int i = 0; i < length; i++)
            digits[i] = s.charAt(i) - '0';
        long total = 0;
        // all shorter numbers, by their first digit
        for (int k = 1; k < length; k++)
            for (int d = 1; d < DIGITS; d++)
                total += complete(new int[] {d}, 1, k);
        // same length: the first position where the number drops below n
        for (int k = 0; k < length; k++) {
            int[] prefix = Arrays.copyOf(digits, length);
            for (int d = k == 0 ? 1 : 0; d < digits[k]; d++) {
                prefix[k] = d;
                total += complete(prefix, k + 1, length);
            }
        }
        return total + complete(digits, length, length);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        if (!in.hasNextLong())
            return;
        long a = in.nextLong(), b = in.nextLong();
        System.out.println(luckyUpTo(b) - luckyUpTo(a - 1));
    }
}
