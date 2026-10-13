import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final int[] ENDS = {1, 2}; // the first and last rows of a best shape are this narrow
    // no k cells have fewer than sqrt(SCALE k - SHIFT) + 2 neighbours
    static final long SCALE = 8, SHIFT = 4;

    static long isqrt(long n) {
        long r = (long)Math.sqrt((double)n);
        while (r * r > n)
            r--;
        while ((r + 1) * (r + 1) <= n)
            r++;
        return r;
    }

    static long capped(int[] full, int cap) {
        long total = 0;
        for (int w : full)
            total += Math.min(w, cap);
        return total;
    }

    // row widths of a region of k cells with the smallest fence: with row ends
    // moving by at most one cell per row the fence is two cells per row plus the
    // first and the last row, and no fence is smaller than sqrt(8 k - 4) + 2
    static int[] widthsFor(long k) {
        for (int fence = (int)isqrt(SCALE * k - SHIFT - 1) + 1 + 2;; fence++)
            for (int first : ENDS)
                for (int last : ENDS) {
                    int twice = fence - first - last, rows = twice / 2;
                    if (twice % 2 != 0 || rows < 1)
                        continue;
                    if (rows == 1 && first != last)
                        continue;
                    int[] full = new int[rows];
                    int widest = 0;
                    for (int i = 0; i < rows; i++) {
                        full[i] =
                            rows == 1 ? first : Math.min(first + 2 * i, last + 2 * (rows - 1 - i));
                        widest = Math.max(widest, full[i]);
                    }
                    if (capped(full, widest) < k)
                        continue;
                    // cap the widest rows at the smallest level that holds k cells
                    int low = Math.max(full[0], full[rows - 1]);
                    int lo = low, hi = widest;
                    while (lo < hi) {
                        int mid = (lo + hi) / 2;
                        if (capped(full, mid) < k)
                            lo = mid + 1;
                        else
                            hi = mid;
                    }
                    int cap = lo;
                    int[] widths = new int[rows];
                    for (int i = 0; i < rows; i++)
                        widths[i] = Math.min(full[i], cap);
                    long extra = capped(full, cap) - k;
                    List<Integer> inner = new ArrayList<>();
                    for (int i = 1; i + 1 < rows; i++)
                        if (widths[i] == cap)
                            inner.add(i);
                    if (cap > low && extra <= inner.size()) {
                        for (int j = 0; j < extra; j++)
                            widths[inner.get(j)]--;
                        return widths;
                    }
                    if (extra == 0)
                        return widths;
                }
    }

    public static void main(String[] args) {
        long k = new Scanner(System.in).nextLong();
        int[] widths = widthsFor(k);
        int rows = widths.length;
        // place the rows from y = 0 up, the first one starting at x = 0; the ends
        // move by at most one cell, the left one first when the row narrows
        int[] left = new int[rows], right = new int[rows];
        right[0] = widths[0] - 1;
        for (int i = 1; i < rows; i++) {
            int grow = widths[i] - (right[i - 1] - left[i - 1] + 1);
            left[i] = left[i - 1] + (grow == 2 ? -1 : (grow < 0 ? 1 : 0));
            right[i] = left[i] + widths[i] - 1;
        }
        int top = rows - 1;
        StringBuilder out = new StringBuilder();
        int count = 0;
        for (int x = left[0]; x <= right[0]; x++, count++)
            out.append(x).append(" -1\n");
        for (int y = 0; y <= top; y++, count++)
            out.append(right[y] + 1).append(' ').append(y).append('\n');
        for (int x = right[top]; x >= left[top]; x--, count++)
            out.append(x).append(' ').append(top + 1).append('\n');
        for (int y = top; y >= 0; y--, count++)
            out.append(left[y] - 1).append(' ').append(y).append('\n');
        System.out.print(count + "\n" + out);
    }
}
