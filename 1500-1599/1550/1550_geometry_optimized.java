import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final double THIRD = 1.0 / 3;
    private static final long SCALE = 100_000L;

    private static double next(BufferedInputStream input, StringBuilder token) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        token.setLength(0);
        while (ch > ' ') {
            token.append((char)ch);
            ch = input.read();
        }
        return Double.parseDouble(token.toString());
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        StringBuilder token = new StringBuilder();
        double h = next(input, token);
        double w = next(input, token);
        double x = next(input, token);
        double y = next(input, token);
        double r = next(input, token);
        double centre = h * (1 - 2 * Math.max(Math.abs(x), Math.abs(y)) / w);
        double volume = h * w * w * THIRD - Math.PI * r * r * centre;
        long scaled = Math.round(volume * SCALE);
        String fraction = Long.toString(SCALE + scaled % SCALE);
        System.out.println(scaled / SCALE + "." + fraction.substring(1));
    }
}
