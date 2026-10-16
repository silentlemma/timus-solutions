import java.util.Scanner;

public class Main {
    static final int LIMB_LIMIT = 1000000;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int k = in.nextInt(), n = in.nextInt();
        // the numbers are kept in limbs of base k^m, the largest power of k up
        // to a million, and digitSum[v] is the sum of the base-k digits of a limb
        int base = 1;
        while (base <= LIMB_LIMIT / k) base *= k;
        int[] digitSum = new int[base];
        for (int v = 1; v < base; v++) digitSum[v] = digitSum[v / k] + v % k;

        int[] cost = new int[n];
        cost[0] = cost[1] = 1;
        // F(n) has fewer than n limbs
        int[] a = new int[n], b = new int[n];
        a[0] = b[0] = 1;
        int length = 1;
        for (int i = 2; i < n; i++) {
            // a, b = b, a + b, summing the digits on the way
            int sum = 0, carry = 0;
            for (int j = 0; j < length; j++) {
                int v = a[j] + b[j] + carry;
                carry = v >= base ? 1 : 0;
                v -= carry * base;
                a[j] = v;
                sum += digitSum[v];
            }
            if (carry == 1) {
                a[length++] = 1;
                sum++;
            }
            int[] swap = a;
            a = b;
            b = swap;
            cost[i] = sum;
        }
        // counting sort by cost keeps equal costs in order of number
        int top = 0;
        for (int c : cost) top = Math.max(top, c);
        int[] start = new int[top + 2];
        for (int c : cost) start[c + 1]++;
        for (int c = 1; c <= top + 1; c++) start[c] += start[c - 1];
        int[] order = new int[n];
        for (int i = 0; i < n; i++) order[start[cost[i]]++] = i + 1;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i > 0) out.append(' ');
            out.append(order[i]);
        }
        System.out.println(out);
    }
}
