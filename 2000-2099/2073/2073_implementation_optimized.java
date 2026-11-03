import java.io.BufferedOutputStream;
import java.util.Arrays;

public class Main {
    static final int NAME_WIDTH = 30, DATE_WIDTH = 8, PROBLEMS = 13;
    static final int WIDTH = NAME_WIDTH + DATE_WIDTH + PROBLEMS + 4;
    static final int DATE_START = NAME_WIDTH + 2, MARK_START = NAME_WIDTH + DATE_WIDTH + 3;
    static final int LINE_BUFFER = 64;
    static int last;
    static final int BUFFER_SIZE = 4096;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        last = c;
        return value;
    }

    static void endLine() throws Exception {
        if (last != '\n' && last >= 0) {
            int ch;
            do {
                ch = read();
            } while (ch >= 0 && ch != '\n');
        }
    }

    static int line(byte[] text) throws Exception {
        int size = 0;
        for (int ch = read(); ch >= 0 && ch != '\n'; ch = read())
            if (ch != '\r')
                text[size++] = (byte)ch;
        return size;
    }

    static void blankRow(byte[] row) {
        Arrays.fill(row, (byte)' ');
        row[0] = row[NAME_WIDTH + 1] = row[NAME_WIDTH + DATE_WIDTH + 2] = row[WIDTH - 1] = '|';
        row[WIDTH] = '\n';
    }

    static void put(byte[] row, int start, String text) {
        for (int i = 0; i < text.length(); i++)
            row[start + i] = (byte)text.charAt(i);
    }

    public static void main(String[] args) throws Exception {
        int n = nextInt();
        endLine();
        byte[] row = new byte[WIDTH + 1], border = new byte[WIDTH + 1],
               text = new byte[LINE_BUFFER];
        blankRow(row);
        for (int i = 0; i < WIDTH; i++)
            border[i] = (byte)(row[i] == '|' ? '+' : '-');
        border[WIDTH] = '\n';
        put(row, 1, "Contest name");
        put(row, DATE_START, "Date");
        for (int i = 0; i < PROBLEMS; i++)
            row[MARK_START + i] = (byte)('A' + i);
        BufferedOutputStream out = new BufferedOutputStream(System.out, BUFFER_SIZE);
        out.write(border);
        out.write(row);
        out.write(border);
        for (int contest = 0; contest < n; contest++) {
            blankRow(row);
            int size = line(text);
            System.arraycopy(text, 0, row, 1, size);
            size = line(text);
            System.arraycopy(text, 0, row, DATE_START, size);
            int p = nextInt(), s = nextInt();
            endLine();
            Arrays.fill(row, MARK_START, MARK_START + p, (byte)'.');
            for (int attempt = 0; attempt < s; attempt++) {
                size = line(text);
                int problem = text[0] - 'A', verdict = 1;
                while (verdict < size && text[verdict] == ' ')
                    verdict++;
                // Only Accepted starts with A among the allowed verdicts.
                if (text[verdict] == 'A')
                    row[MARK_START + problem] = 'o';
                else if (row[MARK_START + problem] != 'o')
                    row[MARK_START + problem] = 'x';
            }
            out.write(row);
            out.write(border);
        }
        out.flush();
    }
}
