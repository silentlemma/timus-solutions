public class Main {
    // the exponent is parsed by hand from System.in, much lighter than Scanner
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
        int exponent = nextInt();
        // by Fermat's last theorem only the first and second powers have answers
        if (exponent == 1) {
            System.out.println("1 2 3");
        } else if (exponent == 2) {
            System.out.println("3 4 5");
        } else {
            System.out.println("-1");
        }
    }
}
