import java.util.Scanner;

public class Main {
    // sin(1-sin(2+sin(3-...sin(n)...))): the sign after k is minus for odd k
    static String sine(int n) {
        StringBuilder s = new StringBuilder();
        for (int k = 1; k <= n; k++) {
            s.append("sin(").append(k);
            if (k < n) {
                s.append(k % 2 == 1 ? '-' : '+');
            }
        }
        for (int k = 0; k < n; k++) {
            s.append(')');
        }
        return s.toString();
    }

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        StringBuilder out = new StringBuilder();
        for (int k = 1; k < n; k++) {
            out.append('(');
        }
        for (int i = 1; i <= n; i++) {
            out.append(sine(i)).append('+').append(n - i + 1);
            if (i < n) {
                out.append(')');
            }
        }
        System.out.println(out);
    }
}
