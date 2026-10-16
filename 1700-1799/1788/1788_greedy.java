import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int sum(int[] values, int count) {
        int total = 0;
        for (int i = 0; i < count; i++) total += values[i];
        return total;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();
        int[] girls = new int[n], boys = new int[m];
        for (int i = 0; i < n; i++) girls[i] = in.nextInt();
        for (int i = 0; i < m; i++) boys[i] = in.nextInt();
        // with k pairs the k most sensitive girls stay dry, and the k most
        // sensitive boys walk with them
        Arrays.sort(girls);
        Arrays.sort(boys);
        int best = Integer.MAX_VALUE;
        for (int k = 0; k <= Math.min(n, m); k++) {
            best = Math.min(best, sum(girls, n - k) + sum(boys, m - k) * k);
        }
        System.out.println(best);
    }
}
