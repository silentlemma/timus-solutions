import java.io.IOException;

public class Main {
    // the numbers are parsed by hand from System.in, much lighter than Scanner
    private static int nextInt() throws IOException {
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = System.in.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value * sign;
    }

    public static void main(String[] args) throws IOException {
        int a1 = nextInt(), b1 = nextInt();
        nextInt();
        int b2 = nextInt(), a3 = nextInt();
        nextInt();
        System.out.println((a1 - a3) + " " + (b1 - b2));
    }
}
