import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // every day uses three pairs and every pair may meet three times,
        // so at most n (n - 1) / 2 days; the triples i, i + d, i + 2d mod n
        // give each pair three meetings: twice as neighbours, once apart
        StringBuilder out = new StringBuilder();
        out.append(n * (n - 1) / 2).append('\n');
        for (int d = 1; d <= (n - 1) / 2; d++) {
            for (int i = 0; i < n; i++) {
                out.append(i + 1).append(' ').append((i + d) % n + 1).append(' ')
                        .append((i + 2 * d) % n + 1).append('\n');
            }
        }
        System.out.print(out);
    }
}
