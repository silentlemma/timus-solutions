public class Main {
    private static final int PAIRS_PER_CAR = 4;
    private static final int SMALLEST = 600;
    // the widest diameter in millimetres
    private static final int LARGEST = 700;

    private static final int BUFFER_SIZE = 1024;
    private static final byte[] buffer = new byte[BUFFER_SIZE];
    private static int position;
    private static int available;

    // the input is read in 1 KB blocks and parsed by hand, which needs much
    // less memory than Scanner
    private static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0) {
                return -1;
            }
        }
        return buffer[position++];
    }

    private static int nextInt() throws java.io.IOException {
        int ch;
        do {
            ch = read();
        } while (ch <= ' ' && ch >= 0);
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt();
        // the diameters are from 600 to 700, so a plain array counts them
        int[] count = new int[LARGEST - SMALLEST + 1];
        for (int i = 0; i < n; ++i) {
            ++count[nextInt() - SMALLEST];
        }
        // each diameter equips as many cars as it has full sets of four pairs
        int cars = 0;
        for (int c : count) {
            cars += c / PAIRS_PER_CAR;
        }
        System.out.println(cars);
    }
}
