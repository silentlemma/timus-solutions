import java.util.Scanner;

public class Main {
    static final int DIGIT = 9; // the largest digit

    public static void main(String[] args) {
        char[] s = new Scanner(System.in).next().toCharArray();
        int after = 0; // the sum of the digits after position i
        // the rightmost digit that can grow by one while the digits after it give
        // one back; the smallest such change gives the next number
        for (int i = s.length - 1; i >= 0; i--) {
            int d = s[i] - '0';
            if (d < DIGIT && after > 0) {
                s[i]++;
                int rest = after - 1;
                // the smallest tail with this sum: the digits pushed to the right
                for (int j = s.length - 1; j > i; j--) {
                    int put = Math.min(DIGIT, rest);
                    s[j] = (char)('0' + put);
                    rest -= put;
                }
                System.out.println(new String(s));
                return;
            }
            after += d;
        }
        System.out.println(-1);
    }
}
