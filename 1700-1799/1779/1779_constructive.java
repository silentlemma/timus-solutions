import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // joining i and j whenever i + j > n gives student i a degree of i up to
        // the middle and i - 1 after it, so only one degree is shared, by two
        StringBuilder out = new StringBuilder();
        int count = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                if (i + j > n) {
                    out.append(i).append(' ').append(j).append('\n');
                    count++;
                }
            }
        }
        System.out.print(count + "\n" + out);
    }
}
