import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int DECIMAL = 10;
    private static final int INPUT_SCALE = 1000;
    private static final int HALF_TURN = 180 * INPUT_SCALE;
    private static final int OUTPUT_SCALE = 10000000;

    private static int thousandths(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        int value = 0;
        int scale = INPUT_SCALE;
        boolean fractional = false;
        while (ch > ' ') {
            if (ch == '.') {
                fractional = true;
            } else {
                value = DECIMAL * value + ch - '0';
                if (fractional) {
                    scale /= DECIMAL;
                }
            }
            ch = input.read();
        }
        return value * scale;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        double radius = thousandths(input) / (double)INPUT_SCALE;
        int angle = thousandths(input);
        int fullChords = HALF_TURN / angle - 1;
        int remainder = HALF_TURN % angle;
        double radiansPerUnit = Math.PI / HALF_TURN;
        double distance = radius * (1 + 2 * (fullChords * Math.sin(angle * radiansPerUnit) +
                                             Math.sin(remainder * radiansPerUnit)));
        long rounded = Math.round(distance * OUTPUT_SCALE);
        String fraction = Long.toString(OUTPUT_SCALE + rounded % OUTPUT_SCALE).substring(1);
        System.out.println(rounded / OUTPUT_SCALE + "." + fraction);
    }
}
