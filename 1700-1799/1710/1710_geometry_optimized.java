import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int BASE = 10;

    private static int number(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        boolean negative = ch == '-';
        if (negative || ch == '+') {
            ch = input.read();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = BASE * value + ch - '0';
            ch = input.read();
        }
        return negative ? -value : value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int ax = number(input), ay = number(input);
        int bx = number(input), by = number(input);
        int dx = number(input) - ax, dy = number(input) - ay;
        int lengthSquared = dx * dx + dy * dy;
        // The second intersection is the reflection across the projection of B onto AC.
        int twiceProjection = 2 * ((bx - ax) * dx + (by - ay) * dy);
        int other = twiceProjection - lengthSquared;
        if (other <= 0 || other == lengthSquared) {
            System.out.println("YES");
            return;
        }
        double x = ax + (double)(dx * other) / lengthSquared;
        double y = ay + (double)(dy * other) / lengthSquared;
        System.out.print(new StringBuilder("NO\n")
                             .append(ax)
                             .append(' ')
                             .append(ay)
                             .append('\n')
                             .append(bx)
                             .append(' ')
                             .append(by)
                             .append('\n')
                             .append(x)
                             .append(' ')
                             .append(y)
                             .append('\n'));
    }
}
