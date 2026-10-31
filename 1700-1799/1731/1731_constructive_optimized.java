public class Main {
    // parse positive decimal tokens directly to avoid scanner allocations.
    private static int nextInt() throws java.io.IOException {
        int c;
        do {
            c = System.in.read();
        } while (c <= ' ' && c != -1);
        int value = 0;
        while (c > ' ') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt(), m = nextInt();
        // with first boxes 1..n and second boxes spaced n apart above them,
        // every sum a + b names its pair, so no two gifts can weigh the same
        StringBuilder out = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            out.append(i).append(i < n ? ' ' : '\n');
        }
        for (int j = 0; j < m; j++) {
            out.append((j + 1) * n + 1).append(j + 1 < m ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
