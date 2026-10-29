public class Main {
    // the numbers are parsed byte by byte from System.in, which needs much
    // less memory than Scanner
    private static int nextInt() throws java.io.IOException {
        int ch;
        do {
            ch = System.in.read();
        } while (ch >= 0 && ch <= ' ');
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int first = nextInt(), last = nextInt();
        // the fuses burn on the odd days; (x + 1) / 2 odd days are in 1..x
        System.out.println((last + 1) / 2 - first / 2);
    }
}
