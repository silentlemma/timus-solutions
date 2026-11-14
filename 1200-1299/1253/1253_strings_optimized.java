import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int LIMIT = 1_000_000;
    private static final int UNVISITED = -1;

    private static int measure(byte[][] templates, int[] lengths, int index) {
        if (lengths[index] != UNVISITED) {
            return lengths[index];
        }
        lengths[index] = LIMIT + 1;
        int length = 0;
        byte[] text = templates[index];
        for (int i = 0; i < text.length; i++) {
            if (text[i] == '*') {
                length += measure(templates, lengths, text[++i] - '0');
            } else {
                length++;
            }
            if (length > LIMIT) {
                return LIMIT + 1;
            }
        }
        return lengths[index] = length;
    }

    private static void emit(byte[][] templates, int[] lengths, int index,
                             BufferedOutputStream output) throws IOException {
        if (lengths[index] == 0) {
            return;
        }
        byte[] text = templates[index];
        int start = 0;
        for (int i = 0; i < text.length; i++) {
            if (text[i] == '*') {
                output.write(text, start, i - start);
                emit(templates, lengths, text[++i] - '0', output);
                start = i + 1;
            }
        }
        output.write(text, start, text.length - start);
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int count = 0;
        for (int c = input.read(); c != '\n' && c != -1; c = input.read()) {
            if (c >= '0' && c <= '9') {
                count = count * 10 + c - '0';
            }
        }
        byte[][] templates = new byte[count + 1][];
        for (int i = 1; i <= count; i++) {
            ByteArrayOutputStream text = new ByteArrayOutputStream();
            for (int c = input.read(); c != '#' && c != -1; c = input.read()) {
                if (c != '\r') {
                    text.write(c);
                }
            }
            templates[i] = text.toByteArray();
            input.mark(2);
            int delimiter = input.read();
            if (delimiter == '\r') {
                delimiter = input.read();
            }
            if (delimiter != '\n' && delimiter != -1) {
                input.reset();
            }
        }
        int[] lengths = new int[count + 1];
        Arrays.fill(lengths, UNVISITED);
        BufferedOutputStream output = new BufferedOutputStream(System.out);
        if (measure(templates, lengths, 1) > LIMIT) {
            output.write('#');
        } else {
            emit(templates, lengths, 1, output);
        }
        output.write('\n');
        output.flush();
    }
}
