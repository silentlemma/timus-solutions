import java.io.IOException;

public class Main {
    static final int LEGS = 40;

    // the numbers are parsed byte by byte from System.in, which needs much
    // less memory than Scanner
    private static int readInt() throws IOException {
        int ch;
        do {
            ch = System.in.read();
        } while (ch <= ' ' && ch != -1);
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int a = readInt();
        int b = readInt();
        // either every right slipper turns up while the left legs are dressed,
        // or 39 rights do, and then every spare left slipper is thrown away
        // before the last right leg is dressed
        System.out.println(Math.max(2 * b + LEGS, 2 * a + LEGS - 1));
    }
}
