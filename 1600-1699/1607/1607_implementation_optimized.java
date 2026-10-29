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
        int petya = nextInt(), raise = nextInt(), driver = nextInt(), discount = nextInt();
        // the driver never asks less than Petya offers, and the other way round
        while (petya < driver) {
            petya += raise;
            if (petya >= driver) {
                petya = driver;
                break;
            }
            driver -= discount;
        }
        System.out.println(petya);
    }
}
