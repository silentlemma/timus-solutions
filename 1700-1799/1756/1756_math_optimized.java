public class Main {

    // refillable storage keeps input memory constant, regardless of input length.
    static final int BUFFER_SIZE = 4096;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int at, size;
    static int read() throws java.io.IOException {
        if (at == size) {
            size = System.in.read(buffer);
            at = 0;
            if (size < 0)
                return -1;
        }
        return buffer[at++];
    }
    static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        boolean negative = c == '-';
        if (negative)
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }

    public static void main(String[] args) throws java.io.IOException {
        long m = nextLong(), firstDays = nextLong(), days = nextLong();
        // the work is m * firstDays digger-days; spreading it as evenly as possible
        // over the given days needs the fewest diggers, the rounded-up average
        long low = m * firstDays / days, extra = m * firstDays % days;
        // format each constant run once; buffering avoids storing the full schedule.
        byte[] lowText = Long.toString(low).getBytes(java.nio.charset.StandardCharsets.US_ASCII);
        byte[] highText =
            Long.toString(low + 1).getBytes(java.nio.charset.StandardCharsets.US_ASCII);
        java.io.BufferedOutputStream out = new java.io.BufferedOutputStream(System.out);
        for (long day = 0; day < days; day++) {
            if (day > 0)
                out.write(' ');
            out.write(day < days - extra ? lowText : highText);
        }
        out.write('\n');
        out.flush();
    }
}
