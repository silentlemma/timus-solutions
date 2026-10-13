import java.util.Scanner;

public class Main {
    // the counts for N = 1 and N = 2; from N = 3 on, 1575 and N - 3 zeros
    static final String[] SMALL = {"", "14", "155"};
    static final int SHORT = 3;
    static final String BASE = "1575";

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        if (n < SHORT) {
            System.out.println(SMALL[n]);
            return;
        }
        StringBuilder out = new StringBuilder(BASE);
        for (int i = SHORT; i < n; i++)
            out.append('0');
        System.out.println(out);
    }
}
