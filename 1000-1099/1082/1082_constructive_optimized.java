public class Main {

    // these inputs contain only nonnegative integers; avoid scanner's regex machinery.
    static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong();
        // on sorted numbers every partition peels off just the first one
        StringBuilder out = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            out.append(i).append(i < n ? " " : "");
        }
        System.out.println(out);
    }
}
