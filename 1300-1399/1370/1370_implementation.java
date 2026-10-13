import java.util.Scanner;

public class Main {
    static final int WINDOW = 10; // digits seen in the window

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();
        String[] digits = new String[n];
        for (int i = 0; i < n; i++)
            digits[i] = in.next();
        // each click moves the window one digit on, around the wheel
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < WINDOW; i++)
            out.append(digits[(m + i) % n]);
        System.out.println(out);
    }
}
