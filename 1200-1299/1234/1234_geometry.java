import java.io.*;
import java.util.*;

public class Main {
    static final int TENTHS = 10, BRICK_SIDES = 3, HOLE_SIDES = 2;

    // whether a p x q rectangle (p >= q) fits into an a x b one (a >= b); a
    // turned fit (p > a, q <= b) needs ((a+b)/(p+q))^2 + ((a-b)/(p-q))^2 >= 2
    // by Carver's criterion, multiplied out here to stay in integers
    static boolean fits(long p, long q, long a, long b) {
        if (q > b)
            return false;
        if (p <= a)
            return true;
        long s = (p + q) * (p + q), d = (p - q) * (p - q);
        return (a + b) * (a + b) * d + (a - b) * (a - b) * s >= 2 * s * d;
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer st =
            new StringTokenizer(new BufferedReader(new InputStreamReader(System.in)).readLine());
        long[] brick = new long[BRICK_SIDES], hole = new long[HOLE_SIDES];
        for (int i = 0; i < brick.length; i++)
            brick[i] = Math.round(Double.parseDouble(st.nextToken()) * TENTHS);
        for (int i = 0; i < hole.length; i++)
            hole[i] = Math.round(Double.parseDouble(st.nextToken()) * TENTHS);
        Arrays.sort(brick);
        Arrays.sort(hole);
        // the face of the two shorter sides is the easiest to put through
        System.out.println(fits(brick[1], brick[0], hole[1], hole[0]) ? "YES" : "NO");
    }
}
