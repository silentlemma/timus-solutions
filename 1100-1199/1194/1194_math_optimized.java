public class Main {
    // the two numbers are parsed by hand from System.in, much lighter than Scanner
    private static long nextInteger() throws java.io.IOException {
        int ch;
        do {
            ch = System.in.read();
        } while (ch != -1 && ch <= ' ');
        long value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        long n = nextInteger();
        long k = nextInteger();
        // every two hobbits shake hands exactly once, when their groups part,
        // except the married couples, who go home together and never part
        System.out.println(n * (n - 1) / 2 - k);
    }
}
