import java.util.Scanner;

public class Main {
    static final int TOP = 30;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] count = new int[TOP + 2];
        for (int i = 0; i < n; i++)
            count[in.nextInt()]++;
        // two types share a symmetric alternating row only as ABA...BA, counts differing by one,
        // along the chain of counts, pairing the leftovers of c with c + 1 at once is best
        int pairs = 0, left = 0;
        for (int c = 1; c <= TOP; c++) {
            int matched = Math.min(left, count[c]);
            pairs += matched;
            left = count[c] - matched;
        }
        System.out.println(n - pairs);
    }
}
