import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int HOUR = 60;
    private static final int DAY = 24 * HOUR;
    private static final int DECIMAL = 10;

    private static int clock(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        int hours = 0;
        while ('0' <= c && c <= '9') {
            hours = hours * DECIMAL + c - '0';
            c = input.read();
        }
        int minutes = 0;
        for (c = input.read(); '0' <= c && c <= '9'; c = input.read()) {
            minutes = minutes * DECIMAL + c - '0';
        }
        return hours * HOUR + minutes;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int departure = clock(input);
        int first = clock(input) - departure;
        departure = clock(input);
        int second = clock(input) - departure;
        // The clock differences differ by twice the shift, within ten minutes.
        int centered = Math.floorMod(first - second + DAY / 2, DAY) - DAY / 2;
        System.out.println((Math.abs(centered) + HOUR) / (2 * HOUR));
    }
}
