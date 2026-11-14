import java.io.BufferedInputStream;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    private static final int ID_BITS = 16;
    private static final int ID_MASK = (1 << ID_BITS) - 1;

    private static int number(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = 10 * value + ch - '0';
            ch = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int stops = number(input), capacity = number(input);
        int requests = number(input), price = number(input);
        char[] starts = new char[stops + 1], ends = new char[stops + 1];
        char[] following = new char[requests + 1];
        int[] finish = new int[requests + 1];
        for (int id = 1; id <= requests; ++id) {
            int start = number(input);
            finish[id] = number(input);
            following[id] = starts[start];
            starts[start] = (char)id;
        }
        boolean[] chosen = new boolean[requests + 1];
        PriorityQueue<Long> farthest = new PriorityQueue<>(Collections.reverseOrder());
        int count = 0, riding = 0;
        for (int stop = 1; stop <= stops; ++stop) {
            riding -= ends[stop];
            for (int id = starts[stop]; id != 0; id = following[id]) {
                int end = finish[id];
                ++ends[end];
                chosen[id] = true;
                ++count;
                // Pack destination and passenger number into one heap key.
                farthest.add(((long)end << ID_BITS) | id);
                if (++riding > capacity) {
                    long drop = farthest.remove();
                    chosen[(int)drop & ID_MASK] = false;
                    --ends[(int)(drop >> ID_BITS)];
                    --riding;
                    --count;
                }
            }
        }
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
        output.write(Long.toString((long)count * price));
        output.newLine();
        String separator = "";
        for (int id = 1; id <= requests; ++id) {
            if (chosen[id]) {
                output.write(separator);
                output.write(Integer.toString(id));
                separator = " ";
            }
        }
        output.newLine();
        output.flush();
    }
}
