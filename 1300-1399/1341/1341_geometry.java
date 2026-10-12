import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final double RADIUS = 6400.0;
    static final double HALF_TURN = 180.0;
    static final double SHOWN = 0.0005; // values that print as 0.000

    // three decimals, without a minus sign on zero
    static String show(double value) {
        return String.format(Locale.US, "%.3f", Math.abs(value) < SHOWN ? 0.0 : value);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        double w = in.nextDouble(), lon = in.nextDouble(), side = in.nextDouble();
        double arc = side / RADIUS; // the angle of one side seen from the center
        double south = w * Math.PI / HALF_TURN, north = south + arc;
        // north and south along meridians cancel; east runs along the northern
        // parallel and west along the southern one, at different speeds
        lon += (arc / Math.cos(north) - arc / Math.cos(south)) * HALF_TURN / Math.PI;
        lon %= 2 * HALF_TURN;
        if (lon > HALF_TURN)
            lon -= 2 * HALF_TURN;
        else if (lon <= -HALF_TURN)
            lon += 2 * HALF_TURN;
        System.out.println(show(w));
        System.out.println(show(lon));
    }
}
