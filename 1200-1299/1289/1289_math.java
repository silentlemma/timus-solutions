import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int half = Integer.parseInt(in.readLine().trim()) / 2;
        // 1 + 9 k^2 with k = 11...1 (half ones), and 9 k^2 = k 10^half - k
        if (half == 0) {
            System.out.println("1");
        } else if (half == 1) {
            System.out.println("10");
        } else {
            StringBuilder answer = new StringBuilder(2 * half);
            for (int i = 0; i < half - 1; i++)
                answer.append('1');
            answer.append('0');
            for (int i = 0; i < half - 2; i++)
                answer.append('8');
            answer.append("90");
            System.out.println(answer);
        }
    }
}
