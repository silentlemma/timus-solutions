import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] weights = new int[n];
        for (int k = 0; k < n; k++) {
            weights[k] = in.nextInt();
        }
        Arrays.sort(weights);
        // each collision takes a square root of the product, so the heaviest
        // stripies should meet first and be rooted the most times
        double total = weights[n - 1];
        for (int k = n - 2; k >= 0; k--) {
            total = 2 * Math.sqrt(total * weights[k]);
        }
        // rounded from the exact binary value, half to even, as printf in C
        System.out.println(
            new BigDecimal(total).setScale(2, RoundingMode.HALF_EVEN).toPlainString());
    }
}
