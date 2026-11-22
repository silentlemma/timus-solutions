public class Main {
    static final int INPUT_CAPACITY = 64, DECIMAL = 10;
    static final byte[] buffer = new byte[INPUT_CAPACITY];
    static int position, available;
    static int read() throws java.io.IOException {
        if (position == available) {
            do {
                available = System.in.read(buffer);
            } while (available == 0);
            position = 0;
            if (available < 0)
                return -1;
        }
        return buffer[position++];
    }
    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        boolean negative = c == '-';
        if (negative || c == '+')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }
    static final double GRAVITY = 9.81, CENTIMETRES = 100, SECONDS = 60;
    static final int STEPS = 60, TURN = 4;
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

    static double endpoint(int index, double quarter) {
        double t = index * quarter;
        return top - GRAVITY * t * t / 2 - ((index & 1) == 0 ? 0 : half);
    }

    static boolean solve(int length, int height, int turns) {
        half = length / CENTIMETRES / 2;
        top = height / CENTIMETRES;
        omega = turns * 2 * Math.PI / SECONDS;
        double quarter = Math.PI / 2 / omega;
        double acceleration = half * omega * omega;
        boolean hasPeak = acceleration > GRAVITY;
        if (!hasPeak) {
            // For acceleration<=g the lowest-end height is strictly decreasing.
            double firstVertical = Math.sqrt(2 * Math.max(0, top - half) / GRAVITY) / quarter;
            int vertical = 1 + 2 * Math.max(0, (int)((firstVertical - 1) / 2));
            while (endpoint(vertical, quarter) > 0)
                vertical += 2;
            while (vertical > 1 && endpoint(vertical - 2, quarter) <= 0)
                vertical -= 2;
            double firstHorizontal = Math.sqrt(2 * top / GRAVITY) / quarter;
            int horizontal = 2 * Math.max(1, (int)(firstHorizontal / 2));
            while (endpoint(horizontal, quarter) > 0)
                horizontal += 2;
            while (horizontal > 2 && endpoint(horizontal - 2, quarter) <= 0)
                horizontal -= 2;
            int inTurn = (Math.min(vertical, horizontal) - 1) % TURN;
            return inTurn == 0 || inTurn == TURN - 1;
        }
        double peakOffset = hasPeak ? Math.asin(GRAVITY / acceleration) / omega : 0;
        // Contact is impossible before the centre descends to half the segment length.
        double earliest = Math.sqrt(2 * Math.max(0, top - half) / GRAVITY);
        int k = Math.max(0, (int)(earliest / quarter) - 1);
        while (true) {
            double a = k * quarter, b = (k + 1) * quarter, lowest = gap(b);
            if (k % 2 == 1 && hasPeak) {
                // On an odd quarter, sin decreases: the slope maximum is explicit.
                double peak = b - peakOffset;
                if (slope(peak, k) > 0) {
                    double lo = a, hi = peak;
                    for (int i = 0; i < STEPS; i++) {
                        double mid = (lo + hi) / 2;
                        if (slope(mid, k) < 0)
                            lo = mid;
                        else
                            hi = mid;
                    }
                    lowest = Math.min(lowest, gap(lo));
                }
            }
            if (lowest <= 0)
                break;
            k++;
        }
        int inTurn = k % TURN;
        return inTurn == 0 || inTurn == TURN - 1;
    }

    public static void main(String[] args) throws java.io.IOException {
        boolean butter = solve(nextInt(), nextInt(), nextInt());
        System.out.write(butter ? new byte[] {'b', 'u', 't', 't', 'e', 'r', '\n'}
                                : new byte[] {'b', 'r', 'e', 'a', 'd', '\n'});
        System.out.flush();
        Runtime.getRuntime().halt(0);
    }
}
