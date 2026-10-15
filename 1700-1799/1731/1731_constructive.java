import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();
        // with first boxes 1..n and second boxes spaced n apart above them,
        // every sum a + b names its pair, so no two gifts can weigh the same
        StringBuilder out = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            out.append(i).append(i < n ? ' ' : '\n');
        }
        for (int j = 0; j < m; j++) {
            out.append((j + 1) * n + 1).append(j + 1 < m ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
