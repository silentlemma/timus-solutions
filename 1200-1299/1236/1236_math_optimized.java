import java.io.IOException;

public class Main {
    static final int MAX_LENGTH = 10000;
    static final int BUFFER_SIZE = 4096;
    static final int HEX_RADIX = 16;
    static final int BYTE_MASK = 255;
    static final String DIGITS = "0123456789ABCDEF";

    static class Input {
        byte[] bytes = new byte[BUFFER_SIZE];
        int position, length;

        int next() throws IOException {
            if (position == length) {
                length = System.in.read(bytes);
                position = 0;
                if (length <= 0)
                    return 0;
            }
            return bytes[position++] & BYTE_MASK;
        }

        int hexValue(int c) {
            if (c <= '9')
                return c - '0';
            return c <= 'F' ? c - 'A' + 10 : c - 'a' + 10;
        }

        int encoded() throws IOException {
            int c = next();
            while (c != 0 && c <= ' ')
                c = next();
            return hexValue(c) * HEX_RADIX + hexValue(next());
        }
    }

    static class Output {
        byte[] bytes = new byte[BUFFER_SIZE];
        int used;

        void flush() throws IOException {
            System.out.write(bytes, 0, used);
            used = 0;
        }

        void key(int value) throws IOException {
            if (used + 2 >= BUFFER_SIZE)
                flush();
            bytes[used++] = (byte)DIGITS.charAt(value / HEX_RADIX);
            bytes[used++] = (byte)DIGITS.charAt(value % HEX_RADIX);
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        byte[] shorter = new byte[MAX_LENGTH];
        int length = 0, c = input.next();
        while (c != 0 && c <= ' ')
            c = input.next();
        while (c > ' ') {
            int high = input.hexValue(c), low = input.hexValue(input.next());
            shorter[length++] = (byte)(high * HEX_RADIX + low);
            c = input.next();
        }
        Output output = new Output();
        int previous = input.encoded() ^ ' ';
        output.key(previous);
        for (int i = 0; i < length; i++) {
            // The plaintext cancels; signed stored bytes are expanded as unsigned values.
            previous ^= (shorter[i] & BYTE_MASK) ^ input.encoded();
            output.key(previous);
        }
        output.bytes[output.used++] = '\n';
        output.flush();
    }
}
