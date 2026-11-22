public class Main {
    static final int FOUR = 4, THREE = 3, TWENTY = 20, FIVE = 5;

    static int nextInt() throws java.io.IOException {
        int c = System.in.read();
        while (c >= 0 && c <= ' ')
            c = System.in.read();
        int n = 0;
        while (c >= '0' && c <= '9') {
            n = n * 10 + c - '0';
            c = System.in.read();
        }
        return n;
    }

    static int zeros(int n) {
        // Modulo 5 decides whether a zero exists. For odd n, the binomial
        // expansion modulo 25 gives 5*n*(1+2^(n-1)); modulo 8 forbids a third.
        if (n % FOUR == 0)
            return 0;
        return n % FOUR == THREE || n % TWENTY == FIVE ? 2 : 1;
    }

    public static void main(String[] args) throws java.io.IOException {
        System.out.write('0' + zeros(nextInt()));
        System.out.write('\n');
    }
}
