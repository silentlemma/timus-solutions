import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long[] sizes = new long[n + 1];
        sizes[0] = in.nextLong();
        for (int i = 1; i <= n; i++) {
            sizes[i] = in.nextLong();
        }
        // each factor is the next one times the size of the next dimension, and
        // the first one times the size of the first dimension is the whole array
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            out.append(i > 0 ? " " : "").append(sizes[i] / sizes[i + 1] - 1);
        }
        System.out.println(out);
    }
}
