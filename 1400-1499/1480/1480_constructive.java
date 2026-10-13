import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        StringBuilder out = new StringBuilder();
        out.append(n * n + n / 2 + 1).append('\n');
        // a chessboard: the large numbers go down on one colour and the small
        // ones up on the other, both in reading order
        int big = n * n, small = 1;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                out.append((i + j) % 2 == 0 ? big-- : small++).append(j + 1 < n ? ' ' : '\n');
        System.out.print(out);
    }
}
