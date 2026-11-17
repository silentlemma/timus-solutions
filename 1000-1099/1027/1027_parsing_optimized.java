import java.io.IOException;
import java.io.InputStream;

public class Main {
    static final int BUFFER_SIZE = 1024;

    static boolean valid(InputStream input) throws IOException {
        byte[] bytes = new byte[BUFFER_SIZE];
        int depth = 0;
        boolean opening = false;
        boolean comment = false;
        boolean star = false;

        for (int length; (length = input.read(bytes)) != -1;) {
            for (int i = 0; i < length; i++) {
                int ch = bytes[i];
                if (comment) {
                    if (star && ch == ')') {
                        comment = false;
                    }
                    star = ch == '*';
                    continue;
                }
                if (opening) {
                    opening = false;
                    if (ch == '*') {
                        comment = true;
                        star = false;
                        continue;
                    }
                    depth++;
                }
                if (ch == '(') {
                    opening = true;
                } else if (ch == ')') {
                    if (depth == 0) {
                        return false;
                    }
                    depth--;
                } else if (depth > 0 && (ch < '0' || ch > '9') && ch != '=' && ch != '+' &&
                           ch != '-' && ch != '*' && ch != '/' && ch != '\r' && ch != '\n') {
                    return false;
                }
            }
        }
        return !opening && !comment && depth == 0;
    }

    public static void main(String[] args) throws IOException {
        System.out.println(valid(System.in) ? "YES" : "NO");
    }
}
