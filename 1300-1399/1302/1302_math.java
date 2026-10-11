import java.util.*;

public class Main {
    // the row of cell n and its two diagonal strips, from the left and from
    // the right; one step across an edge changes exactly one of them
    static long[] strips(long n) {
        long row = (long)Math.sqrt((double)(n - 1));
        while (row * row > n - 1)
            row--;
        while ((row + 1) * (row + 1) <= n - 1)
            row++;
        row++;
        long place = n - (row - 1) * (row - 1); // 1 .. 2 row - 1 within the row
        return new long[] {row, (place + 1) / 2, (2 * row - place + 1) / 2};
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long[] a = strips(in.nextLong()), b = strips(in.nextLong());
        long total = 0;
        for (int i = 0; i < a.length; i++)
            total += Math.abs(a[i] - b[i]);
        System.out.println(total);
    }
}
