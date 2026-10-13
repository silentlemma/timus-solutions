import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final double TURN = 2 * Math.PI;
    static final long SCALE = 1000000;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        double x0 = in.nextDouble(), y0 = in.nextDouble(), eps = in.nextDouble();
        eps = Math.min(eps, 1);
        double across = Math.asin(Math.max(-1, Math.min(1, x0)));
        double up = Math.acos(Math.max(-1, Math.min(1, y0)));
        // take sqrt(t) = s0 with sin(s0) = x0 and s0 > 2 pi / eps; within pi of
        // t0 = s0^2 some t has cos(t) = y0, and sqrt(t) moves by less than eps / 4
        double s0 = across + TURN * (Math.ceil(1 / eps) + 1);
        double t0 = s0 * s0;
        double t = up + TURN * Math.floor((t0 - up) / TURN + 0.5);
        long ticks = (long) Math.floor(t * SCALE + 0.5);
        System.out.println(String.format(Locale.US, "%d.%06d", ticks / SCALE, ticks % SCALE));
    }
}
