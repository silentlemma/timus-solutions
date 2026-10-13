import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final long SCALE = 100; // coordinates come with two decimals: work in hundredths

    static long hundredths(String s) {
        int dot = s.indexOf('.');
        String whole = dot < 0 ? s : s.substring(0, dot);
        String part = ((dot < 0 ? "" : s.substring(dot + 1)) + "00").substring(0, 2);
        long p = Long.parseLong(part);
        return Long.parseLong(whole) * SCALE + (s.startsWith("-") ? -p : p);
    }

    // The face A x B in the middle of the column lies at z = 0 with its
    // corner (c, b + c) at the origin; every other face folds up from it.
    static long[] fold(long a, long b, long c, long x, long y) {
        if (x < c)
            return new long[] {0, y - b - c, c - x};
        if (x > c + a)
            return new long[] {a, y - b - c, x - c - a};
        if (y < b)
            return new long[] {x - c, b - y, c};
        if (y < b + c)
            return new long[] {x - c, 0, b + c - y};
        if (y <= 2 * b + c)
            return new long[] {x - c, y - b - c, 0};
        return new long[] {x - c, b, y - 2 * b - c};
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long a = in.nextLong() * SCALE, b = in.nextLong() * SCALE, c = in.nextLong() * SCALE;
        long[] p = fold(a, b, c, hundredths(in.next()), hundredths(in.next()));
        long[] q = fold(a, b, c, hundredths(in.next()), hundredths(in.next()));
        long squared = 0;
        for (int i = 0; i < p.length; i++)
            squared += (p[i] - q[i]) * (p[i] - q[i]);
        System.out.println(String.format(Locale.US, "%.10f", Math.sqrt(squared) / SCALE));
    }
}
