public class Main {
    static final int BUFFER_SIZE = 32, RADIX = 10, PLACES = 6;
    static final int SCALE = 1_000_000, QUARTER_SCALE = SCALE / 4;
    // One unit in the integer result is a millionth of the area.
    static final double CROSS_SCALE = 707_106.7811865475; // SCALE / sqrt(2)
    static final double ROUND_HALF = 0.5;

    public static void main(String[] args) throws Exception {
        byte[] buffer = new byte[BUFFER_SIZE];
        int a = 0, b = 0;
    // Both lengths are positive. Keep a partial token across short reads.
    input:
        for (int size; (size = System.in.read(buffer)) != -1;) {
            for (int i = 0; i < size; i++) {
                int c = buffer[i];
                if (c >= '0' && c <= '9') {
                    b = b * RADIX + (c - '0');
                } else if (b != 0) {
                    if (a != 0)
                        break input;
                    a = b;
                    b = 0;
                }
            }
        }
        long squareTerm = (long)(a * a + b * b) * QUARTER_SCALE;
        long micros = squareTerm + (long)((a * b) * CROSS_SCALE + ROUND_HALF);
        int whole = (int)(micros / SCALE);
        int fraction = (int)(micros - (long)whole * SCALE);

        int pos = buffer.length;
        buffer[--pos] = '\n';
        for (int i = 0; i < PLACES; i++) {
            buffer[--pos] = (byte)('0' + fraction % RADIX);
            fraction /= RADIX;
        }
        buffer[--pos] = '.';
        do {
            buffer[--pos] = (byte)('0' + whole % RADIX);
            whole /= RADIX;
        } while (whole != 0);
        System.out.write(buffer, pos, buffer.length - pos);
        System.out.flush();
    }
}
