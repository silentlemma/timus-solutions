public class Main {
    // parse decimal tokens directly without allocating scanner machinery.
    private static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = System.in.read();
        } while (c <= ' ' && c != -1);
        long value = 0;
        while (c > ' ') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong();
        long previous = nextLong();
        StringBuilder output = new StringBuilder();
        // each factor is the next one times the size of the next dimension, and
        // the first one times the size of the first dimension is the whole array
        for (int i = 0; i < n; i++) {
            long current = nextLong();
            if (i > 0)
                output.append(' ');
            output.append(previous / current - 1);
            previous = current;
        }
        System.out.println(output);
    }
}
