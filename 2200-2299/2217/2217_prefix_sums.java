import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        String s = in.readLine().trim();
        int zeros = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0') {
                zeros++;
            }
        }
        if (n % 2 == 0 && zeros % 2 != 0) {
            System.out.println("NO");
            return;
        }

        int balance = 0;
        for (int i = 0; i < n / 2; i++) {
            // A zero can move left, so the suffix must supply at least as many zeros.
            if (s.charAt(n - 1 - i) == '0') {
                balance++;
            }
            if (s.charAt(i) == '0') {
                balance--;
            }
            if (balance < 0) {
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }
}
