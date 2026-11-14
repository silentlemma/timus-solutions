import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int PER_METRE = 9;
    private static final int LANE_TIME = 72;
    private static final int CAR_LENGTH = 5;
    private static final int INTERVAL_WIDTH = LANE_TIME + PER_METRE * CAR_LENGTH;
    private static final int UNITS_PER_SECOND = 50;
    private static final int HUNDREDTHS = 100;

    private static int number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = input.read();
        }
        return value;
    }

    private static int[] readLane(BufferedInputStream input, int shift) throws IOException {
        int[] starts = new int[number(input)];
        for (int i = 0; i < starts.length; i++) {
            starts[i] = PER_METRE * number(input) - shift;
        }
        return starts;
    }

    private static int earliest(int[] near, int[] far) {
        int i = 0, j = 0, wait = 0;
        while (i < near.length || j < far.length) {
            int start;
            if (j == far.length || (i < near.length && near[i] <= far[j])) {
                start = near[i++];
            } else {
                start = far[j++];
            }
            if (start >= wait) {
                break;
            }
            wait = Math.max(wait, start + INTERVAL_WIDTH);
        }
        return wait;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int[] near = readLane(input, LANE_TIME);
        int[] far = readLane(input, 2 * LANE_TIME);
        int wait = earliest(near, far);
        int fraction = wait % UNITS_PER_SECOND * (HUNDREDTHS / UNITS_PER_SECOND);
        System.out.println(wait / UNITS_PER_SECOND + "." + (fraction < 10 ? "0" : "") + fraction +
                           "0000");
    }
}
