import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;
import java.util.Locale;

public class Main {
    // times in units of 1/50 s: a car (20 km/h) covers a metre in 9 units and
    // Egor (5 km/h) crosses a 2 m lane in 72
    static final int METRE = 9;
    static final int LANE = 72;
    static final int CAR = 5;
    static final double UNITS = 50;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        int[][] blocked = new int[0][];
        // a car is on the crossing from METRE d to METRE (d + CAR); a start time
        // s is bad when Egor's time in the car's lane overlaps that
        for (int lane = 0; lane < 2; lane++) {
            in.nextToken();
            int count = (int) in.nval;
            int[][] more = Arrays.copyOf(blocked, blocked.length + count);
            for (int i = 0; i < count; i++) {
                in.nextToken();
                int d = (int) in.nval;
                int enter = lane * LANE;
                more[blocked.length + i] =
                    new int[] {METRE * d - enter - LANE, METRE * (d + CAR) - enter};
            }
            blocked = more;
        }
        Arrays.sort(blocked, (a, b) -> Integer.compare(a[0], b[0]));
        int start = 0;
        for (int[] b : blocked) {
            if (b[0] >= start) {
                break;
            }
            start = Math.max(start, b[1]);
        }
        System.out.println(String.format(Locale.US, "%.6f", start / UNITS));
    }
}
