import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {
    // common pieces of English, tried along with the frequent words of the text
    static final String[] PIECES = {
        "\n", " the ", "the ", " and ", "ing ", " of ", " to ", "ed ", "he ", "th", "in",
        "er", "an",    "re",   "on",    "at",   "en",   "nd",   "es",  "or",  "ou", "ha",
        "is", "it",    "te",   "st",    "ar",   "al",   "le",   "se",  "ve",  "me", "ne",
        "hi", "as",    "ng",   "e ",    "s ",   "d ",   "t ",   ", ",  ". ",  "y ", "o ",
    };
    static final int LINE = 17; // a table line without its piece: '    t[NNN] = "";' and a line end
    static final int CHUNK = 1000; // characters of the coded text per string literal
    static final int WORDS = 300;  // the most promising words of the text that are tried

    static final int FIRST = 33, LAST = 126; // printable characters that may become codes
    static final String SPECIAL = "\"\\?";   // need a backslash inside a C string
    static final int START = 1 << 18;        // more than the longest text

    static OutputStream out = new BufferedOutputStream(System.out);

    static void write(String s) throws IOException {
        for (int i = 0; i < s.length(); i++)
            out.write(s.charAt(i));
    }

    // the text as it is written inside a C string literal
    static void writeLiteral(byte[] text, int from, int to) throws IOException {
        for (int i = from; i < to; i++) {
            byte ch = text[i];
            if (ch == '\n') {
                write("\\n");
                continue;
            }
            if (SPECIAL.indexOf(ch) >= 0)
                out.write('\\');
            out.write(ch);
        }
    }

    static int writtenLength(byte[] piece) {
        int n = 0;
        for (byte b : piece)
            n += (b == '\n' || SPECIAL.indexOf(b) >= 0) ? 2 : 1;
        return n;
    }

    static boolean startsWith(byte[] text, int at, int length, byte[] piece) {
        if (at + piece.length > length)
            return false;
        for (int k = 0; k < piece.length; k++) {
            if (text[at + k] != piece[k])
                return false;
        }
        return true;
    }

    // uses of a piece, counted left to right without overlaps
    static int count(byte[] text, int length, byte[] piece) {
        int uses = 0;
        for (int at = 0; at < length;) {
            if (startsWith(text, at, length, piece)) {
                uses++;
                at += piece.length;
            } else {
                at++;
            }
        }
        return uses;
    }

    // the end of the word that starts at at: past the space it may start
    // with, then past its letters
    static int wordEnd(byte[] text, int length, int at) {
        int end = text[at] == ' ' ? at + 1 : at;
        while (end < length && isLetter(text[end]))
            end++;
        return end;
    }

    // the words starting at a and b compared byte by byte
    static int compareWords(byte[] text, int length, int a, int b) {
        int endA = wordEnd(text, length, a), endB = wordEnd(text, length, b);
        for (; a < endA && b < endB; a++, b++) {
            if (text[a] != text[b])
                return text[a] - text[b];
        }
        return (endA - a) - (endB - b);
    }

    // the starts of the words of two letters or more, each first with the
    // space before it if there is one; only counts them when starts is null
    static int scan(byte[] text, int length, int[] starts) {
        int found = 0;
        for (int i = 0; i < length;) {
            if (!isLetter(text[i])) {
                i++;
                continue;
            }
            int j = i;
            while (j < length && isLetter(text[j]))
                j++;
            if (j - i >= 2) {
                if (i > 0 && text[i - 1] == ' ') {
                    if (starts != null)
                        starts[found] = i - 1;
                    found++;
                }
                if (starts != null)
                    starts[found] = i;
                found++;
            }
            i = j;
        }
        return found;
    }

    interface Order {
        boolean before(int a, int b);
    }

    // heapsort in place: no extra memory and no boxed numbers
    static void sort(int[] a, int n, Order order) {
        for (int i = n / 2 - 1; i >= 0; i--)
            sift(a, i, n, order);
        for (int end = n - 1; end > 0; end--) {
            int t = a[0];
            a[0] = a[end];
            a[end] = t;
            sift(a, 0, end, order);
        }
    }

    static void sift(int[] a, int i, int n, Order order) {
        for (int child = 2 * i + 1; child < n; i = child, child = 2 * i + 1) {
            if (child + 1 < n && order.before(a[child], a[child + 1]))
                child++;
            if (!order.before(a[i], a[child]))
                return;
            int t = a[i];
            a[i] = a[child];
            a[child] = t;
        }
    }

    static boolean isLetter(byte ch) {
        return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z');
    }

    static class Candidate {
        String piece;
        int estimate;

        Candidate(String piece, int estimate) {
            this.piece = piece;
            this.estimate = estimate;
        }
    }

    // by the estimated saving, then by the piece; a class, not a lambda,
    // since the lambda machinery alone takes much of the 4 MB
    static final Comparator<Candidate> BETTER = new Comparator<Candidate>() {
        public int compare(Candidate a, Candidate b) {
            if (a.estimate != b.estimate)
                return a.estimate > b.estimate ? -1 : 1;
            return a.piece.compareTo(b.piece);
        }
    };

    public static void main(String[] args) throws IOException {
        InputStream in = System.in;
        byte[] text = new byte[START];
        int length = 0;
        for (int n = 0; n >= 0; n = in.read(text, length, text.length - length)) {
            length += n;
            if (length == text.length)
                text = Arrays.copyOf(text, 2 * length);
        }
        int kept = 0;
        boolean[] used = new boolean[LAST + 1];
        for (int i = 0; i < length; i++) {
            if (text[i] == '\r')
                continue;
            text[kept++] = text[i];
            if (text[i] >= 0 && text[i] <= LAST)
                used[text[i]] = true;
        }
        length = kept;
        final byte[] all = text;
        final int size = length;
        // the words of the text, with the space before them and without, kept
        // as their starts alone; sorting them groups equal ones
        final int[] starts = new int[scan(text, length, null)];
        scan(text, length, starts);
        sort(starts, starts.length, new Order() {
            public boolean before(int a, int b) {
                return compareWords(all, size, a, b) < 0;
            }
        });
        // one group per distinct word, moved to the front of starts, and its
        // estimated saving: every use saves the word's length less one
        int distinct = 0;
        for (int i = 0; i < starts.length; i++) {
            if (i == 0 || compareWords(text, length, starts[i - 1], starts[i]) != 0)
                distinct++;
        }
        final int[] saving = new int[distinct];
        for (int i = 0, g = -1; i < starts.length; i++) {
            if (g < 0 || compareWords(text, length, starts[g], starts[i]) != 0)
                starts[++g] = starts[i];
            saving[g] += wordEnd(text, length, starts[g]) - starts[g] - 1;
        }
        int[] rank = new int[distinct];
        for (int g = 0; g < distinct; g++)
            rank[g] = g;
        sort(rank, distinct, new Order() {
            public boolean before(int a, int b) {
                if (saving[a] != saving[b])
                    return saving[a] > saving[b];
                return compareWords(all, size, starts[a], starts[b]) < 0;
            }
        });
        List<Candidate> words = new ArrayList<>();
        for (int k = 0; k < Math.min(WORDS, distinct); k++) {
            int at = starts[rank[k]];
            String word = new String(text, at, wordEnd(text, length, at) - at, "ISO-8859-1");
            words.add(new Candidate(word, saving[rank[k]]));
        }
        // a piece made only of characters of the text can never match a code
        List<Candidate> order = new ArrayList<>();
        for (String pieceText : PIECES) {
            boolean fits = true;
            for (int k = 0; k < pieceText.length(); k++)
                fits = fits && used[pieceText.charAt(k)];
            if (fits) {
                byte[] piece = pieceText.getBytes("ISO-8859-1");
                int estimate = count(text, length, piece) * (writtenLength(piece) - 1);
                order.add(new Candidate(pieceText, estimate));
            }
        }
        for (Candidate w : words) {
            boolean known = false;
            for (Candidate c : order) {
                if (c.piece.equals(w.piece)) {
                    c.estimate = Math.max(c.estimate, w.estimate);
                    known = true;
                }
            }
            if (!known)
                order.add(w);
        }
        Collections.sort(order, BETTER);
        int nextFree = FIRST;
        StringBuilder table = new StringBuilder();
        for (Candidate c : order) {
            while (nextFree <= LAST && (used[nextFree] || SPECIAL.indexOf(nextFree) >= 0))
                nextFree++;
            if (nextFree > LAST)
                break;
            byte[] piece = c.piece.getBytes("ISO-8859-1");
            int written = writtenLength(piece);
            // every use saves the written length of the piece less one character
            if (count(text, length, piece) * (written - 1) <= LINE + written)
                continue;
            byte code = (byte)nextFree++;
            // replace in place, left to right: the text only gets shorter
            int write = 0;
            for (int read = 0; read < length; write++) {
                if (startsWith(text, read, length, piece)) {
                    text[write] = code;
                    read += piece.length;
                } else {
                    text[write] = text[read++];
                }
            }
            length = write;
            StringBuilder escaped = new StringBuilder();
            for (byte b : piece) {
                if (b == '\n') {
                    escaped.append("\\n");
                } else {
                    if (SPECIAL.indexOf(b) >= 0)
                        escaped.append('\\');
                    escaped.append((char)b);
                }
            }
            table.append("    t[").append(code).append("] = \"").append(escaped).append("\";\n");
        }
        write("//CPP\n#include <cstdio>\nconst char *d[] = {\n");
        for (int i = 0; i < length; i += CHUNK) {
            out.write('"');
            writeLiteral(text, i, Math.min(length, i + CHUNK));
            write("\",\n");
        }
        write("0};\nint main() {\n    const char *t[256] = {0};\n");
        write(table.toString());
        write("    for (int k = 0; d[k]; k++)\n");
        write("        for (const char *p = d[k]; *p; p++)\n");
        write("            if (t[(unsigned char)*p]) fputs(t[(unsigned char)*p], stdout);\n");
        write("            else putchar(*p);\n");
        write("    return 0;\n}\n");
        out.flush();
    }
}
