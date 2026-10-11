import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class Main {
    // common pieces of English, tried in this order; each one that pays off
    // gets a printable character the text never uses
    static final String[] PIECES = {
        "\n", " the ", "the ", " and ", "ing ", " of ", " to ", "ed ", "he ", "th", "in",
        "er", "an",    "re",   "on",    "at",   "en",   "nd",   "es",  "or",  "ou", "ha",
        "is", "it",    "te",   "st",    "ar",   "al",   "le",   "se",  "ve",  "me", "ne",
        "hi", "as",    "ng",   "e ",    "s ",   "d ",   "t ",   ", ",  ". ",  "y ", "o ",
    };
    static final int ENTRY = 24; // the size of one table line, so a piece must save more than this
    static final int CHUNK = 1000; // characters of the coded text per string literal

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

    static boolean startsWith(byte[] text, int at, int length, byte[] piece) {
        if (at + piece.length > length)
            return false;
        for (int k = 0; k < piece.length; k++) {
            if (text[at + k] != piece[k])
                return false;
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        InputStream in = System.in;
        byte[] text = new byte[START];
        int length = 0;
        for (int n = 0; n >= 0; n = in.read(text, length, text.length - length)) {
            length += n;
            if (length == text.length)
                text = java.util.Arrays.copyOf(text, 2 * length);
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
        int nextFree = FIRST;
        StringBuilder table = new StringBuilder();
        for (String pieceText : PIECES) {
            while (nextFree <= LAST && (used[nextFree] || SPECIAL.indexOf(nextFree) >= 0))
                nextFree++;
            if (nextFree > LAST)
                break;
            byte[] piece = pieceText.getBytes("ISO-8859-1");
            int uses = 0, written = 0;
            for (int at = 0; at < length;) {
                if (startsWith(text, at, length, piece)) {
                    uses++;
                    at += piece.length;
                } else {
                    at++;
                }
            }
            for (byte b : piece)
                written += (b == '\n' || SPECIAL.indexOf(b) >= 0) ? 2 : 1;
            // every use saves the written length of the piece less one character
            if (uses * (written - 1) <= ENTRY)
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
