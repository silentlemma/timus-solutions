import java.util.*;

public class Main {
    static final long BASE = 3;

    public static void main(String[] args) {
        long n = new Scanner(System.in).nextLong(), pay = 0, tip = 0;
        // balanced ternary: digits 1 go into the payment, digits -1 into the tip
        for (long power = 1; n > 0; power *= BASE) {
            if (n % BASE == 1) {
                pay += power;
                n--;
            } else if (n % BASE == BASE - 1) {
                tip += power;
                n++;
            }
            n /= BASE;
        }
        // no tip yet: add the smallest bill the payment lacks to both
        for (long power = 1; tip == 0; power *= BASE) {
            if (pay / power % BASE == 0) {
                pay += power;
                tip = power;
            }
        }
        System.out.println(pay + " " + tip);
    }
}
