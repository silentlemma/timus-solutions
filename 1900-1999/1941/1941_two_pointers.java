import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int LOWEST_SYMBOL = 33;
    private static final int SYMBOL_COUNT = 90;
    private static final int LETTER_WIDTH = 3;
    private static final int ALPHABET_SIZE = SYMBOL_COUNT * SYMBOL_COUNT * SYMBOL_COUNT;
    private static final int MAX_PATTERN = 8000;
    private final int[] deficit = new int[ALPHABET_SIZE];
    private final int[] ring;
    private int missing;
    private int position;
    private int used;

    Main(int[] pattern, int size) {
        ring = new int[size];
        missing = size;
        for (int index = 0; index < size; ++index)
            ++deficit[pattern[index]];
    }

    boolean push(int code) {
        if (used == ring.length) {
            int old = ring[position];
            if (deficit[old] >= 0)
                ++missing;
            ++deficit[old];
        } else {
            ++used;
        }
        if (deficit[code] > 0)
            --missing;
        --deficit[code];
        ring[position] = code;
        if (++position == ring.length)
            position = 0;
        return missing == 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream in = new BufferedInputStream(System.in);
        int[] pattern = new int[MAX_PATTERN];
        int size = 0, width = 0, code = 0, ch;
        while ((ch = in.read()) != -1 && ch != '\n') {
            if (ch <= ' ')
                continue;
            code = code * SYMBOL_COUNT + ch - LOWEST_SYMBOL;
            if (++width == LETTER_WIDTH) {
                pattern[size++] = code;
                width = 0;
                code = 0;
            }
        }
        Main counter = new Main(pattern, size);
        int answer = 0;
        while ((ch = in.read()) != -1) {
            if (ch <= ' ')
                continue;
            code = ch - LOWEST_SYMBOL;
            for (int index = 1; index < LETTER_WIDTH; ++index) {
                code = code * SYMBOL_COUNT + in.read() - LOWEST_SYMBOL;
            }
            if (counter.push(code))
                ++answer;
        }
        System.out.println(answer);
    }
}
