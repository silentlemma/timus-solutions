import java.io.*;

public class Main {
    static final int PERIOD = 6; // the simple pattern fails exactly when n mod 6 is 2

    // the row of the queen in each column 1 ... n for even n; the main
    // diagonal stays free
    static int[] evenRows(int n) {
        int half = n / 2;
        int[] rows = new int[n];
        for (int i = 1; i <= half; i++)
            if (n % PERIOD != 2) {
                // the even rows in the left half, the odd rows in the right half
                rows[i - 1] = 2 * i;
                rows[half + i - 1] = 2 * i - 1;
            } else {
                int shift = (2 * (i - 1) + half - 1) % n;
                rows[i - 1] = 1 + shift;
                rows[n - i] = n - shift;
            }
        return rows;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        // an odd board is an even one plus the free corner (n, n)
        int[] rows = evenRows(n - n % 2);
        StringBuilder sb = new StringBuilder();
        for (int col = 1; col <= n; col++)
            sb.append(col).append(' ').append(col <= rows.length ? rows[col - 1] : n).append('\n');
        System.out.print(sb);
    }
}
