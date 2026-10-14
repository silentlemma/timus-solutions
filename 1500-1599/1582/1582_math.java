import java.util.*;

public class Main {
    static final double TOTAL = 1000, HALF = 0.5;
    static final int OUTCOMES = 3;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        double inverse = 0;
        for (int i = 0; i < OUTCOMES; i++)
            inverse += 1 / in.nextDouble();
        // betting in proportion to 1 / k on every outcome pays the same whatever
        // happens, and any other split pays less on some outcome
        System.out.println((long)Math.floor(TOTAL / inverse + HALF));
    }
}
