public class Main {
    static final int[] NOTES = {10, 50, 100, 500, 1000, 5000};

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
        long total = 0, smallest = 0;
        for (int note : NOTES) {
            long count = nextInt();
            total += count * note;
            if (count > 0 && smallest == 0)
                smallest = note;
        }
        long price = nextInt();
        // k tickets fit when k * price <= total, and taking away the smallest
        // note must leave too little: total - smallest < k * price
        long low = (total - smallest) / price + 1, high = total / price;
        StringBuilder out = new StringBuilder();
        out.append(high - low + 1).append('\n');
        for (long k = low; k <= high; k++) {
            if (k > low)
                out.append(' ');
            out.append(k);
        }
        System.out.println(out);
    }
}
