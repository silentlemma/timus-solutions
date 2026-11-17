import java.io.IOException;
import java.io.InputStream;

public class Main {
    static final int DECIMAL = 10;
    static final int ROD_SUM = 1 + 2 + 3;

    static int readNumber(InputStream input) throws IOException {
        int ch;
        do {
            ch = input.read();
        } while (ch >= 0 && ch <= ' ');
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = DECIMAL * value + ch - '0';
            ch = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        InputStream input = System.in;
        byte[] rods = new byte[readNumber(input)];
        for (int i = 0; i < rods.length; i++) {
            rods[i] = (byte)readNumber(input);
        }
        int source = 1;
        int target = 2;
        int step = 0;
        for (int i = rods.length - 1; i >= 0; i--) {
            if (rods[i] == target) {
                step = (step << 1) + 1;
                source = ROD_SUM - source - target;
            } else if (rods[i] == source) {
                step <<= 1;
                target = ROD_SUM - source - target;
            } else {
                System.out.println(-1);
                return;
            }
        }
        System.out.println(step);
    }
}
