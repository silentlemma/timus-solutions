import java.util.Scanner;

public class Main {
    static final int ONE_DIGIT = 4; // floors 1 to 5 show every indicator lit and unlit

    static final int SHORT = 5; // blocks of the second digit: 6 through 9, 0 to 2
    static final int LONG = 7;  // blocks of the second digit: 2 to 9, 0

    static final int LOW_TOP = 3; // a leading digit up to this needs blank, 1, 2 on top
    static final int WIDE = 3;    // blocks of the leading digit otherwise: blank through 4

    public static void main(String[] args) {
        String n = new Scanner(System.in).next();
        int digits = n.length();
        if (digits == 1) {
            System.out.println(ONE_DIGIT);
            return;
        }
        int top = n.charAt(0) - '0', second = n.charAt(1) - '0';
        int lead, zeros;
        if (top == 1) {
            lead = second >= 2 ? SHORT : LONG;
            zeros = digits - 2;
        } else {
            lead = top <= LOW_TOP ? 1 : WIDE;
            zeros = digits - 1;
        }
        // lead * 10^zeros + 1, written out
        if (zeros == 0) {
            System.out.println(lead + 1);
        } else {
            StringBuilder out = new StringBuilder().append(lead);
            for (int i = 1; i < zeros; i++)
                out.append('0');
            System.out.println(out.append('1'));
        }
    }
}
