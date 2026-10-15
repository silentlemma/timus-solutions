import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long ax = in.nextLong();
        long ay = in.nextLong();
        long bx = in.nextLong();
        long by = in.nextLong();
        long cx = in.nextLong();
        long cy = in.nextLong();
        // C' on the ray AC with |BC'| = |BC| is the other root t of
        // t^2 - 2 t (AB . u) + |AB|^2 - |BC|^2 = 0, u the unit vector along AC:
        // t' = 2 (AB . AC) / |AC| - |AC|, so C' = A + (C - A) (2 dot - |AC|^2) / |AC|^2
        long dot = (bx - ax) * (cx - ax) + (by - ay) * (cy - ay);
        long side = (cx - ax) * (cx - ax) + (cy - ay) * (cy - ay);
        if (2 * dot <= side || dot == side) {
            System.out.println("YES");
            return;
        }
        double k = (double) (2 * dot - side) / side;
        StringBuilder out = new StringBuilder("NO\n");
        out.append(String.format(Locale.US, "%.10f %.10f%n", (double) ax, (double) ay));
        out.append(String.format(Locale.US, "%.10f %.10f%n", (double) bx, (double) by));
        double x = ax + (cx - ax) * k;
        double y = ay + (cy - ay) * k;
        out.append(String.format(Locale.US, "%.10f %.10f%n", x, y));
        System.out.print(out);
    }
}
