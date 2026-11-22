public class Main {
    static final int BUFFER_SIZE = 4096, BYTE_MASK = 255;
    static final byte[] input = new byte[BUFFER_SIZE], output = new byte[BUFFER_SIZE];
    static int position, available, used;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++] & BYTE_MASK;
    }
    static void emit(int c) throws java.io.IOException {
        if (used == output.length) {
            System.out.write(output, 0, used);
            used = 0;
        }
        output[used++] = (byte)c;
    }
    static int next(byte[] word) throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        if (c < 0)
            return -1;
        int size = 0;
        while (c > ' ') {
            word[size++] = (byte)c;
            c = read();
        }
        return size;
    }
    public static void main(String[] args) throws java.io.IOException {
        int c = read(), n = 0;
        while (c >= 0 && c <= ' ')
            c = read();
        while (c >= '0' && c <= '9') {
            n = 10 * n + c - '0';
            c = read();
        }
        byte[] word = new byte[n + 1];
        for (int size; (size = next(word)) >= 0;) {
            int weight = 0, mod = n + 1, edit = -1, digit = 0;
            for (int i = 0; i < size; i++)
                if (word[i] == '1')
                    weight += i + 1;
            if (size == n) {
                int raised = weight % mod;
                if (raised != 0)
                    word[raised - 1] = '0';
            } else if (size == n - 1) {
                int after = 0;
            search:
                for (int i = size; i >= 0; i--) {
                    for (int d = 0; d <= 1; d++)
                        if ((weight + after + d * (i + 1)) % mod == 0) {
                            edit = i;
                            digit = '0' + d;
                            break search;
                        }
                    if (i > 0 && word[i - 1] == '1')
                        after++;
                }
            } else {
                int after = 0;
                for (int i = size - 1; i >= 0; i--) {
                    int d = word[i] - '0';
                    if ((weight - after - d * (i + 1)) % mod == 0) {
                        edit = i;
                        break;
                    }
                    after += d;
                }
            }
            // Emit the one edit directly; no substring, concatenation or UTF-8 copy.
            for (int i = 0; i <= size; i++) {
                if (size == n - 1 && i == edit)
                    emit(digit);
                if (i < size && (size != n + 1 || i != edit))
                    emit(word[i]);
            }
            emit('\n');
        }
        System.out.write(output, 0, used);
        System.out.flush();
    }
}
