public class Main {
    static int nextInt() throws Exception {
        int c = System.in.read();
        while (c <= ' ')
            c = System.in.read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }
    public static void main(String[] args) throws Exception {
        int n = nextInt(), k = nextInt();
        // The uncovered square has side min(N mod K, K - N mod K).
        int remainder = n % k, side = Math.min(remainder, k - remainder);
        System.out.println(n < k ? 0 : (n * n - side * side) / k);
    }
}
