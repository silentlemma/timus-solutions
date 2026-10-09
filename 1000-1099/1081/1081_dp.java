import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long k = in.nextLong();
        // count[r]: strings of length r without two adjacent ones (Fibonacci)
        List<Long> count = new ArrayList<>();
        count.add(1L);
        count.add(2L);
        while (count.size() <= n) {
            count.add(count.get(count.size() - 1) + count.get(count.size() - 2));
        }
        if (k > count.get(n)) {
            System.out.println(-1);
            return;
        }
        StringBuilder out = new StringBuilder();
        char last = '0';
        for (int pos = 0; pos < n; pos++) {
            long rest = count.get(n - pos - 1);
            // strings with 0 here come first; a 1 is only possible after a 0
            if (last == '1' || k <= rest) {
                last = '0';
            } else {
                k -= rest;
                last = '1';
            }
            out.append(last);
        }
        System.out.println(out);
    }
}
