public class Main {
    public static void main(String[] args) throws java.io.IOException {
        // the number is parsed byte by byte from System.in, which needs much less
        // memory than Scanner
        long n = 0;
        int sign = 1;
        int c = System.in.read();
        while (c >= 0 && c <= ' ')
            c = System.in.read();
        if (c == '-') {
            sign = -1;
            c = System.in.read();
        }
        while (c >= '0' && c <= '9') {
            n = n * 10 + c - '0';
            c = System.in.read();
        }
        n *= sign;
        // the numbers between 1 and N form one interval whichever side N is on,
        // and its sum is the count times the average of the ends
        long count = Math.abs(n - 1) + 1;
        System.out.println((1 + n) * count / 2);
    }
}
