public class Main {
    static final int BUFFER_SIZE = 4096;
    static byte[] input = new byte[BUFFER_SIZE];
    static int position, available;
    static int read() throws Exception {
        if (position >= available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }
    static int nextInt() throws Exception {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        if (c < 0)
            return -1;
        int result = 0;
        while (c >= '0' && c <= '9') {
            result = result * 10 + c - '0';
            c = read();
        }
        return result;
    }
    public static void main(String[] args) throws Exception {
        StringBuilder output = new StringBuilder();
        while (true) {
            long n = nextInt();
            if (n < 0)
                break;
            long p = nextInt();
            if (n == 0 && p == 0)
                break;
            long result = n >= p ? 0 : 1, i = 2;
            // The paired product is below2e17; promote every factor tolong.
            for (; i + 1 <= n && result != 0; i += 2)
                result = result * i * (i + 1) % p;
            if (i <= n && result != 0)
                result = result * i % p;
            output.append(result).append('\n');
        }
        System.out.print(output);
    }
}
