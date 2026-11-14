import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static final int DIVISOR_THREE = 3;
    private static final int DECIMAL = 10;
    private static final int DIGITS_PER_ROW = 6;

    private static void writeRow(BufferedOutputStream out, byte[] digits, int row)
        throws IOException {
        int offset = digits.length;
        while (row > 0) {
            digits[--offset] = (byte)('0' + row % DECIMAL);
            row /= DECIMAL;
        }
        out.write(digits, offset, digits.length - offset);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int size = Integer.parseInt(input.readLine().trim());
        if (size % 2 == 0 || size % DIVISOR_THREE == 0) {
            System.out.println("No");
            return;
        }

        BufferedOutputStream out = new BufferedOutputStream(System.out);
        out.write('Y');
        out.write('e');
        out.write('s');
        out.write('\n');
        byte[] digits = new byte[DIGITS_PER_ROW];
        // The modular sequence visits the odd rows, then the even rows.
        for (int first = 1; first <= 2; first++) {
            for (int row = first; row <= size; row += 2) {
                if (row != 1) {
                    out.write(' ');
                }
                writeRow(out, digits, row);
            }
        }
        out.write('\n');
        out.flush();
    }
}
