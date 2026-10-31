import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    static final int INITIAL_PILES = 3;

    // these inputs contain only nonnegative integers; avoid scanner's regex machinery.
    static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        List<Long> piles = new ArrayList<>();
        for (int i = 0; i < INITIAL_PILES; i++)
            piles.add(nextLong());
        int asked = 0;
        while (true) {
            asked++;
            // the closest two piles differ least among neighbours in sorted order
            Collections.sort(piles);
            long gap = Long.MAX_VALUE;
            for (int i = 1; i < piles.size(); i++) {
                gap = Math.min(gap, piles.get(i) - piles.get(i - 1));
            }
            if (gap == 0)
                break;
            piles.add(gap);
        }
        System.out.println(asked);
    }
}
