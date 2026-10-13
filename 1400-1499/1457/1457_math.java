import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long sum = 0;
        for (int i = 0; i < n; i++)
            sum += in.nextLong();
        // the mean of squared distances is smallest at the arithmetic mean
        System.out.printf(Locale.US, "%.6f%n", (double)sum / n);
    }
}
