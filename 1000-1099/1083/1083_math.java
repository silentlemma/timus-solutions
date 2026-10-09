import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.next().length();
        // multiply n, n - k, ... while the factor stays positive
        long product = 1;
        for (int factor = n; factor > 0; factor -= k) {
            product *= factor;
        }
        System.out.println(product);
    }
}
