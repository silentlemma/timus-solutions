import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    // whether one side of some inscribed square passes through both points:
    // a side lies on a line at distance R / sqrt(2) from the centre, and the
    // disc cuts exactly the side out of that line
    static boolean sameSide(long r, long x1, long y1, long x2, long y2) {
        if (x1 == x2 && y1 == y2) {
            return 2 * (x1 * x1 + y1 * y1) >= r * r;
        }
        long cross = x1 * y2 - y1 * x2;
        long dx = x1 - x2;
        long dy = y1 - y2;
        return 2 * cross * cross == r * r * (dx * dx + dy * dy);
    }

    static long next(StreamTokenizer in) throws IOException {
        in.nextToken();
        return (long) in.nval;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        long t = next(in);
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < t; i++) {
            long r = next(in);
            long x1 = next(in);
            long y1 = next(in);
            long x2 = next(in);
            long y2 = next(in);
            // the second point on the same, the opposite or an adjacent side:
            // turning it by 0, 180, 90 or -90 degrees brings it onto the first one's side
            boolean ok = sameSide(r, x1, y1, x2, y2) || sameSide(r, x1, y1, -x2, -y2)
                    || sameSide(r, x1, y1, -y2, x2) || sameSide(r, x1, y1, y2, -x2);
            out.append(ok ? "YES" : "NO").append('\n');
        }
        System.out.print(out);
    }
}
