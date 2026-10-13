import java.util.Scanner;

public class Main {
    static final int HALF = 1000, TICKETS = 1000000, BASE = 10;

    static int digitSum(int n) {
        int s = 0;
        for (; n > 0; n /= BASE)
            s += n % BASE;
        return s;
    }

    static boolean lucky(int n) { return digitSum(n / HALF) == digitSum(n % HALF); }

    public static void main(String[] args) {
        int number = Integer.parseInt(new Scanner(System.in).next());
        // the sums differ by one, so the ticket is neither 000000 nor 999999
        // and both neighbours are six-digit tickets
        boolean yes = false;
        for (int n : new int[] {number - 1, number + 1})
            if (n >= 0 && n < TICKETS && lucky(n))
                yes = true;
        System.out.println(yes ? "Yes" : "No");
    }
}
