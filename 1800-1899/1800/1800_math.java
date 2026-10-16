import java.util.Scanner;

public class Main {
    static final double GRAVITY = 9.81, CENTIMETRES = 100, SECONDS = 60;
    static final int STEPS = 100, TURN = 4;
    static double half, top, omega;

    // the height of the lowest end of the toast at time t
    static double gap(double t) {
        return top - GRAVITY * t * t / 2 - half * Math.abs(Math.sin(omega * t));
    }

    // d gap / dt in quarter k, where the angle within the half turn is
    // omega*t - (k / 2)*pi
    static double slope(double t, int k) {
        return -GRAVITY * t - half * omega * Math.cos(omega * t - (k / 2) * Math.PI);
    }

    // d slope / dt, falling through an odd quarter
    static double bend(double t, int k) {
        return -GRAVITY + half * omega * omega * Math.sin(omega * t - (k / 2) * Math.PI);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int length = in.nextInt(), height = in.nextInt(), turns = in.nextInt();
        half = length / CENTIMETRES / 2;
        top = height / CENTIMETRES;
        omega = turns * 2 * Math.PI / SECONDS;
        double quarter = Math.PI / 2 / omega;
        int k = 0;
        while (true) {
            double a = k * quarter, b = (k + 1) * quarter, lowest = gap(b);
            if (k % 2 == 1) {
                // the end rises again here: the slope of the gap is concave, so
                // find its peak; where it turns positive, the gap has a minimum
                double lo = a, hi = b;
                for (int i = 0; i < STEPS; i++) {
                    double mid = (lo + hi) / 2;
                    if (bend(mid, k) > 0) {
                        lo = mid;
                    } else {
                        hi = mid;
                    }
                }
                if (slope(lo, k) > 0) {
                    hi = lo;
                    lo = a;
                    for (int i = 0; i < STEPS; i++) {
                        double mid = (lo + hi) / 2;
                        if (slope(mid, k) < 0) {
                            lo = mid;
                        } else {
                            hi = mid;
                        }
                    }
                    lowest = Math.min(lowest, gap(lo));
                }
            }
            if (lowest <= 0) break;
            k++;
        }
        // in quarters 0 and 3 of a turn the butter faces down
        int inTurn = k % TURN;
        System.out.println(inTurn == 0 || inTurn == TURN - 1 ? "butter" : "bread");
    }
}
