public class Main {
    static int prefix(int label) {
        int half = label / 2, cost = 2 * (half - Integer.bitCount(half));
        // A final even label contributes just its left adjacent gap.
        if (label % 2 == 0)
            cost -= Integer.numberOfTrailingZeros(label) - 1;
        return cost;
    }
    static int nextInt() throws Exception {
        int c = System.in.read();
        while (c <= ' ')
            c = System.in.read();
        int result = 0;
        while (c >= '0' && c <= '9') {
            result = result * 10 + c - '0';
            c = System.in.read();
        }
        return result;
    }
    public static void main(String[] args) throws Exception {
        int a = nextInt(), b = nextInt();
        System.out.println(Math.abs(prefix(a) - prefix(b)));
    }
}
