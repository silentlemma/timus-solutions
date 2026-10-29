import java.io.BufferedOutputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;

public class Main {
    static final int MAX_NAME = 200;
    static final String[] HOUSES = {"Slytherin", "Hufflepuff", "Gryffindor", "Ravenclaw"};
    static final int BUFFER_SIZE = 4096;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, length;

    // the input is read in 4 KB blocks and the names are copied as bytes into
    // one byte stream per house, with no String objects
    static int readByte() throws IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length < 0)
                return -1;
        }
        return buffer[position++];
    }

    static int readLine(byte[] line) throws IOException {
        int size = 0, c;
        while ((c = readByte()) >= 0 && c != '\n') {
            if (c != '\r')
                line[size++] = (byte)c;
        }
        return size;
    }

    public static void main(String[] args) throws IOException {
        byte[] line = new byte[MAX_NAME + 1];
        int length = readLine(line), n = 0;
        for (int i = 0; i < length; i++) {
            if (line[i] >= '0' && line[i] <= '9')
                n = n * 10 + line[i] - '0';
        }
        ByteArrayOutputStream[] lists = new ByteArrayOutputStream[HOUSES.length];
        for (int h = 0; h < HOUSES.length; h++)
            lists[h] = new ByteArrayOutputStream();
        byte[] house = new byte[MAX_NAME + 1];
        for (int i = 0; i < n; i++) {
            // names keep their inner spaces, so only the line break is dropped
            length = readLine(line);
            readLine(house);
            int start = 0;
            while (house[start] <= ' ')
                start++;
            for (int h = 0; h < HOUSES.length; h++) {
                if (house[start] == HOUSES[h].charAt(0)) {
                    lists[h].write(line, 0, length);
                    lists[h].write('\n');
                }
            }
        }
        BufferedOutputStream out = new BufferedOutputStream(System.out, BUFFER_SIZE);
        for (int h = 0; h < HOUSES.length; h++) {
            if (h > 0)
                out.write('\n');
            out.write(HOUSES[h].getBytes("US-ASCII"));
            out.write(':');
            out.write('\n');
            lists[h].writeTo(out);
        }
        out.flush();
    }
}
