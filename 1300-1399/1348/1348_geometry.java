import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long ax = in.nextLong(), ay = in.nextLong(), bx = in.nextLong(), by = in.nextLong();
        long cx = in.nextLong(), cy = in.nextLong(), rope = in.nextLong();
        long dx = bx - ax, dy = by - ay, length = dx * dx + dy * dy;
        // the nearest point of the bed: C projected onto AB, kept inside it
        double t = 0;
        if (length != 0)
            t = Math.max(0.0, Math.min(1.0, (double)((cx - ax) * dx + (cy - ay) * dy) / length));
        double nearest = Math.hypot(ax + t * dx - cx, ay + t * dy - cy);
        double farthest = Math.max(Math.hypot(ax - cx, ay - cy), Math.hypot(bx - cx, by - cy));
        System.out.println(String.format(Locale.US, "%.2f", Math.max(0.0, nearest - rope)));
        System.out.println(String.format(Locale.US, "%.2f", Math.max(0.0, farthest - rope)));
    }
}
