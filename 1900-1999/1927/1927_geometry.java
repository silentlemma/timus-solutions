import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final int SEGMENT_COORDINATES = 4;

    static double intersectionArea(long[] first, long[] second) {
        long vx = first[2] - first[0];
        long vy = first[SEGMENT_COORDINATES - 1] - first[1];
        long wx = second[2] - second[0];
        long wy = second[SEGMENT_COORDINATES - 1] - second[1];
        long determinant = vx * wy - vy * wx;
        if (determinant != 0) {
            long numerator = (vx * vx + vy * vy) * (wx * wx + wy * wy);
            return (double) numerator / Math.abs(determinant);
        }
        long a = vx * first[0] + vy * first[1];
        long b = vx * first[2] + vy * first[SEGMENT_COORDINATES - 1];
        long c = vx * second[0] + vy * second[1];
        long d = vx * second[2] + vy * second[SEGMENT_COORDINATES - 1];
        return Math.max(Math.min(a, b), Math.min(c, d))
                < Math.min(Math.max(a, b), Math.max(c, d)) ? -1 : 0;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        long[] first = new long[SEGMENT_COORDINATES];
        long[] second = new long[SEGMENT_COORDINATES];
        for (int i = 0; i < SEGMENT_COORDINATES; i++) {
            first[i] = input.nextLong();
        }
        for (int i = 0; i < SEGMENT_COORDINATES; i++) {
            second[i] = input.nextLong();
        }
        System.out.printf(Locale.US, "%.10f%n", intersectionArea(first, second));
    }
}
