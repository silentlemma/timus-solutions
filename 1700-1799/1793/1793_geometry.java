import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long a = in.nextLong(), b = in.nextLong(), d = in.nextLong();
        long r1 = in.nextLong(), top1 = in.nextLong();
        long r2 = in.nextLong(), top2 = in.nextLong();
        long h = in.nextLong();
        // the widest part of a plate inside the borders, at height min(d, h),
        // scaled by h to stay in integers
        long low = Math.min(d, h);
        long w1 = r1 * h + (top1 - r1) * low, w2 = r2 * h + (top2 - r2) * low;
        boolean fits = 2 * Math.max(w1, w2) <= Math.min(a, b) * h;
        // the centres can be this far apart along each side, and the plates
        // must be at least top1 + top2 apart, where they are widest
        long dx = a * h - w1 - w2, dy = b * h - w1 - w2, need = (top1 + top2) * h;
        boolean apart = dx * dx + dy * dy >= need * need;
        System.out.println(fits && apart ? "YES" : "NO");
    }
}
