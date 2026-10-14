import java.io.*;
import java.util.*;

public class Main {
    // what is known about a set of words, one bit each: is it non-empty, does
    // it hold the empty word, does it hold a non-empty word, is it infinite
    static final int ANY = 1, EMPTY = 2, LONG = 4, INFINITE = 8;
    static final int NOTHING = 0, EMPTY_WORD = ANY | EMPTY, LETTER = ANY | LONG;

    static int unite(int x, int y) { return x | y; }

    static int concat(int x, int y) {
        if ((x & ANY) == 0 || (y & ANY) == 0)
            return NOTHING;
        return ANY | (x & y & EMPTY) | ((x | y) & (LONG | INFINITE));
    }

    // repeating a non-empty word gives ever longer words
    static int star(int x) { return (x & LONG) != 0 ? ANY | EMPTY | LONG | INFINITE : EMPTY_WORD; }

    // one level of brackets: the union so far, the concatenation so far and
    // the last symbol, which a star may still apply to
    static class Frame {
        int all = NOTHING, cat = EMPTY_WORD, last = NOTHING;
        boolean hasLast = false;

        int close() { return unite(all, hasLast ? concat(cat, last) : cat); }

        void push(int symbol) {
            if (hasLast)
                cat = concat(cat, last);
            last = symbol;
            hasLast = true;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        ArrayDeque<Frame> frames = new ArrayDeque<>();
        frames.push(new Frame());
        int c;
        while ((c = in.read()) != -1) {
            Frame frame = frames.peek();
            if (c == '(')
                frames.push(new Frame());
            else if (c == ')') {
                frames.pop();
                frames.peek().push(frame.close());
            } else if (c == '|') {
                frame.all = frame.close();
                frame.cat = EMPTY_WORD;
                frame.hasLast = false;
            } else if (c == '*')
                frame.last = star(frame.last);
            else if (c == '0')
                frame.push(NOTHING);
            else if (c >= 'a' && c <= 'z')
                frame.push(LETTER);
        }
        System.out.println((frames.peek().close() & INFINITE) != 0 ? "N" : "F");
    }
}
