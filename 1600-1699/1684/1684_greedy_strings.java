import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;

public class Main {
    static final int MAX_LENGTH = 75000, BUFFER_SIZE = 4096, CUT = 1 << 31;
    static final BufferedInputStream input = new BufferedInputStream(System.in, BUFFER_SIZE);

    static int token(byte[] target) throws Exception {
        int c = input.read(), n = 0;
        while (c <= ' ')
            c = input.read();
        while (c > ' ') {
            target[n++] = (byte)c;
            c = input.read();
        }
        return n;
    }

    public static void main(String[] args) throws Exception {
        byte[] word = new byte[MAX_LENGTH], text = new byte[MAX_LENGTH];
        int size = token(word), n = token(text);
        int[] prefix = new int[size], matched = new int[n + 1];
        for (int i = 1; i < size; i++) {
            int k = prefix[i - 1];
            while (k > 0 && word[k] != word[i])
                k = prefix[k - 1];
            if (word[k] == word[i])
                k++;
            prefix[i] = k;
        }
        int k = 0;
        for (int end = 1; end <= n; end++) {
            while (k > 0 && (k == size || word[k] != text[end - 1]))
                k = prefix[k - 1];
            if (word[k] == text[end - 1])
                k++;
            matched[end] = k;
        }
        for (int end = n; end > 0;) {
            int length = matched[end];
            if (length == 0) {
                System.out.println("Yes");
                return;
            }
            // All lengths are positive 17-bit values; sign bit records a cut.
            matched[end] |= CUT;
            end -= length;
        }
        BufferedOutputStream out = new BufferedOutputStream(System.out, BUFFER_SIZE);
        out.write('N');
        out.write('o');
        out.write('\n');
        int begin = 0;
        for (int end = 1; end <= n; end++)
            if ((matched[end] & CUT) != 0) {
                if (begin > 0)
                    out.write(' ');
                out.write(text, begin, end - begin);
                begin = end;
            }
        out.write('\n');
        out.flush();
    }
}
