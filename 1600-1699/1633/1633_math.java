import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long a1 = in.nextLong(), b1 = in.nextLong(), a2 = in.nextLong(), b2 = in.nextLong();
        // the largest singular value of [[a1, b1], [a2, b2]] without cancellation:
        // both sums of squares are exact integers
        long p = (a1 + b2) * (a1 + b2) + (b1 - a2) * (b1 - a2);
        long q = (a1 - b2) * (a1 - b2) + (b1 + a2) * (b1 + a2);
        double norm = (Math.sqrt(p) + Math.sqrt(q)) / 2;
        System.out.println(String.format(Locale.US, "%.10f", norm));
    }
}
