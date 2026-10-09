import java.util.Scanner;

public class Main {
    static int[] digits(int v, int base) {
        int len = 0;
        for (int t = v; t > 0; t /= base) {
            len++;
        }
        int[] out = new int[len];
        for (int i = len - 1; i >= 0; i--, v /= base) {
            out[i] = v % base;
        }
        return out;
    }

    static boolean fits(int x, int y, int base) {
        int[] dx = digits(x, base), dy = digits(y, base);
        int j = 0;
        for (int i = 0; i < dx.length && j < dy.length; i++) {
            if (dx[i] == dy[j]) {
                j++;
            }
        }
        return j == dy.length;
    }

    static int answer(int x, int y) {
        int base = 2;
        for (; (long)base * base <= x; base++) {
            if (fits(x, y, base)) {
                return base;
            }
        }
        // from here on x has two digits x / b and x % b, and y must be one of them
        int best = 0;
        int low = Math.max(base, x / (y + 1) + 1);
        if (low <= x / y) {
            best = low;
        }
        // x % b == y means that b divides x - y and is larger than y
        int least = Math.max(base, y + 1), n = x - y;
        for (int d = 1; d * d <= n; d++) {
            if (n % d == 0) {
                for (int b : new int[] {d, n / d}) {
                    if (b >= least && (best == 0 || b < best)) {
                        best = b;
                    }
                }
            }
        }
        return best;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int x = in.nextInt(), y = in.nextInt();
        int best = answer(x, y);
        System.out.println(best == 0 ? "No solution" : String.valueOf(best));
    }
}
