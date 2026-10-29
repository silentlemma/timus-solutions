public class Main {
    private static final int HALF = 1000;

    // the six digits are parsed byte by byte from System.in instead of Scanner
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

    private static int digitSum(int number) {
        int sum = 0;
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        return sum;
    }

    private static boolean lucky(int number) {
        return digitSum(number / HALF) == digitSum(number % HALF);
    }

    public static void main(String[] args) throws java.io.IOException {
        int number = nextInt();
        // the sums differ by one, so the ticket is neither 000000 nor 999999
        // and both neighbours are six-digit tickets
        System.out.println(lucky(number - 1) || lucky(number + 1) ? "Yes" : "No");
    }
}
