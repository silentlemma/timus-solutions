import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Locale;

public class Main {
    private static final int LINE_COUNT = 3;
    private static final int COORDINATES_PER_LINE = 4;
    private static final int END_Y_INDEX = 3;
    private static final int OUTPUT_DIGITS = 15;
    private static final double ROTATION_COSINE = 0.5;
    private static final double ROTATION_SINE = Math.sqrt(3.0) / 2;

    private static double cross(double[] first, double[] second) {
        return first[0] * second[1] - first[1] * second[0];
    }

    private static long integerArea(long[] line, long x, long y) {
        return (line[2] - line[0]) * (y - line[1]) - (line[END_Y_INDEX] - line[1]) * (x - line[0]);
    }

    private static double[] rotate(double[] vector, int orientation) {
        double sine = orientation * ROTATION_SINE;
        return new double[] {ROTATION_COSINE * vector[0] - sine * vector[1],
                             sine * vector[0] + ROTATION_COSINE * vector[1]};
    }

    private static double[][] equilateralPoints(long[][] lines) {
        long[] first = lines[0];
        long[] second = lines[1];
        long[] third = lines[2];
        boolean useBeginning = Math.abs(integerArea(second, first[0], first[1]))
            >= Math.abs(integerArea(second, first[2], first[END_Y_INDEX]));
        double[] base = useBeginning ? new double[] {first[0], first[1]}
                                    : new double[] {first[2], first[END_Y_INDEX]};
        double[] anchorSecond = {second[0], second[1]};
        double[] anchorThird = {third[0], third[1]};
        double[] directionSecond = {second[2] - second[0], second[END_Y_INDEX] - second[1]};
        double[] directionThird = {third[2] - third[0], third[END_Y_INDEX] - third[1]};
        double[] positive = rotate(directionSecond, 1);
        double[] negative = rotate(directionSecond, -1);
        boolean usePositive = Math.abs(cross(positive, directionThird))
            >= Math.abs(cross(negative, directionThird));
        int orientation = usePositive ? 1 : -1;
        double[] direction = usePositive ? positive : negative;
        double[] offset = rotate(new double[] {anchorSecond[0] - base[0],
                                               anchorSecond[1] - base[1]}, orientation);
        double[] rotatedAnchor = {base[0] + offset[0], base[1] + offset[1]};
        double[] delta = {anchorThird[0] - rotatedAnchor[0], anchorThird[1] - rotatedAnchor[1]};
        double determinant = cross(direction, directionThird);
        double secondParameter = cross(delta, directionThird) / determinant;
        double thirdParameter = cross(delta, direction) / determinant;
        double[] pointSecond = {anchorSecond[0] + secondParameter * directionSecond[0],
                                anchorSecond[1] + secondParameter * directionSecond[1]};
        double[] pointThird = {anchorThird[0] + thirdParameter * directionThird[0],
                               anchorThird[1] + thirdParameter * directionThird[1]};
        return new double[][] {base, pointSecond, pointThird};
    }

    private static long nextLong(BufferedInputStream input) throws IOException {
        int symbol;
        do {
            symbol = input.read();
        } while (symbol <= ' ' && symbol >= 0);
        boolean negative = symbol == '-';
        if (negative) {
            symbol = input.read();
        }
        long value = 0;
        while (symbol > ' ') {
            value = value * 10 + symbol - '0';
            symbol = input.read();
        }
        return negative ? -value : value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        long[][] lines = new long[LINE_COUNT][COORDINATES_PER_LINE];
        for (int index = 0; index < LINE_COUNT; index++) {
            for (int coordinate = 0; coordinate < COORDINATES_PER_LINE; coordinate++) {
                lines[index][coordinate] = nextLong(input);
            }
        }
        String format = "%." + OUTPUT_DIGITS + "f %." + OUTPUT_DIGITS + "f%n";
        for (double[] point : equilateralPoints(lines)) {
            System.out.printf(Locale.US, format, point[0], point[1]);
        }
    }
}
