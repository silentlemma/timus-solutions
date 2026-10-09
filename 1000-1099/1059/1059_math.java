import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // Horner's scheme: ((a0 * X + a1) * X + a2) ... in reverse Polish notation
        StringBuilder out = new StringBuilder("0\n");
        for (int i = 1; i <= n; i++) {
            out.append("X\n*\n").append(i).append("\n+\n");
        }
        System.out.print(out);
    }
}
