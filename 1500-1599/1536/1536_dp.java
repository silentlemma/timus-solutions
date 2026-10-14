import java.io.*;
import java.util.*;

public class Main {
    // the places a stick can take in one cell of the picture
    static final int TOP = 1, MIDDLE = 1 << 1, BOTTOM = 1 << 2, UPPER_LEFT = 1 << 3;
    static final int UPPER_RIGHT = 1 << 4, LOWER_LEFT = 1 << 5, LOWER_RIGHT = 1 << 6;
    static final int UPPER_SLASH = 1 << 7, LOWER_SLASH = 1 << 8, PLUS_UPRIGHT = 1 << 9;
    static final int EQUAL_UPPER = 1 << 10, EQUAL_LOWER = 1 << 11;
    static final int SIDES = UPPER_LEFT | UPPER_RIGHT | LOWER_LEFT | LOWER_RIGHT;
    static final int[] DIGIT_SHAPE = {
        TOP | SIDES | BOTTOM,
        UPPER_SLASH | UPPER_RIGHT | LOWER_RIGHT,
        TOP | UPPER_RIGHT | LOWER_SLASH | BOTTOM,
        TOP | UPPER_SLASH | MIDDLE | LOWER_SLASH,
        UPPER_LEFT | UPPER_RIGHT | MIDDLE | LOWER_RIGHT,
        TOP | UPPER_LEFT | MIDDLE | LOWER_RIGHT | BOTTOM,
        UPPER_SLASH | MIDDLE | LOWER_LEFT | LOWER_RIGHT | BOTTOM,
        TOP | UPPER_SLASH | LOWER_LEFT,
        TOP | SIDES | MIDDLE | BOTTOM,
        TOP | UPPER_LEFT | UPPER_RIGHT | MIDDLE | LOWER_SLASH,
    };
    static final int PLUS_SHAPE = MIDDLE | PLUS_UPRIGHT; // the bar lies where a middle stick does
    static final int EQUAL_SHAPE = EQUAL_UPPER | EQUAL_LOWER;
    static final int LONGEST = 8; // digits in a number
    static final int BASE = 10;
    static final int NONE = -1;

    static int[] cells;

    static int shapeOf(char c) {
        return c == '+' ? PLUS_SHAPE : c == '=' ? EQUAL_SHAPE : DIGIT_SHAPE[c - '0'];
    }

    static int kept(int pos, int shape) { return Integer.bitCount(cells[pos] & shape); }

    // how a state was reached: the digits of its column and the previous state
    static class Step {
        final int dx, dy, dz, carry, used;

        Step(int dx, int dy, int dz, int carry, int used) {
            this.dx = dx;
            this.dy = dy;
            this.dz = dz;
            this.carry = carry;
            this.used = used;
        }
    }

    static String solve(String text, int k) {
        int n = text.length(), total = 0;
        cells = new int[n];
        for (int i = 0; i < n; i++)
            total += Integer.bitCount(cells[i] = shapeOf(text.charAt(i)));
        for (int lenX = 1; lenX <= LONGEST; lenX++)
            for (int lenY = 1; lenY <= LONGEST; lenY++) {
                int lenZ = n - 2 - lenX - lenY;
                // no leading zeros, so z has at least as many digits as x and y
                if (lenZ < Math.max(lenX, lenY) || lenZ > LONGEST)
                    continue;
                int plus = lenX, equal = lenX + lenY + 1;
                // best[col][carry][used]: sticks kept in place after col columns
                // from the right, with the digits and the previous state in from
                int[][][] best = new int[lenZ + 1][2][total + 1];
                Step[][][] from = new Step[lenZ + 1][2][total + 1];
                for (int[][] a : best)
                    for (int[] b : a)
                        Arrays.fill(b, NONE);
                best[0][0][Integer.bitCount(PLUS_SHAPE) + Integer.bitCount(EQUAL_SHAPE)] =
                    kept(plus, PLUS_SHAPE) + kept(equal, EQUAL_SHAPE);
                for (int col = 0; col < lenZ; col++) {
                    int posX = col < lenX ? lenX - 1 - col : NONE;
                    int posY = col < lenY ? lenX + lenY - col : NONE;
                    int posZ = n - 1 - col;
                    for (int carry = 0; carry < 2; carry++)
                        for (int used = 0; used <= total; used++) {
                            int have = best[col][carry][used];
                            if (have == NONE)
                                continue;
                            for (int dx = 0; dx < (posX == NONE ? 1 : BASE); dx++) {
                                if (posX != NONE && dx == 0 && col == lenX - 1 && lenX > 1)
                                    continue;
                                for (int dy = 0; dy < (posY == NONE ? 1 : BASE); dy++) {
                                    if (posY != NONE && dy == 0 && col == lenY - 1 && lenY > 1)
                                        continue;
                                    int sum = dx + dy + carry, dz = sum % BASE, out = sum / BASE;
                                    if (dz == 0 && col == lenZ - 1 && lenZ > 1)
                                        continue;
                                    int more = Integer.bitCount(DIGIT_SHAPE[dz]);
                                    int gain = kept(posZ, DIGIT_SHAPE[dz]);
                                    if (posX != NONE) {
                                        more += Integer.bitCount(DIGIT_SHAPE[dx]);
                                        gain += kept(posX, DIGIT_SHAPE[dx]);
                                    }
                                    if (posY != NONE) {
                                        more += Integer.bitCount(DIGIT_SHAPE[dy]);
                                        gain += kept(posY, DIGIT_SHAPE[dy]);
                                    }
                                    if (used + more > total)
                                        continue;
                                    if (best[col + 1][out][used + more] < have + gain) {
                                        best[col + 1][out][used + more] = have + gain;
                                        from[col + 1][out][used + more] =
                                            new Step(dx, dy, dz, carry, used);
                                    }
                                }
                            }
                        }
                }
                // every stick must be used, and the moved ones are those not kept
                int last = best[lenZ][0][total];
                if (last == NONE || total - last > k)
                    continue;
                char[] x = new char[lenX], y = new char[lenY], z = new char[lenZ];
                int carry = 0, used = total;
                for (int col = lenZ; col > 0; col--) {
                    Step s = from[col][carry][used];
                    int c = col - 1;
                    if (c < lenX)
                        x[lenX - 1 - c] = (char)('0' + s.dx);
                    if (c < lenY)
                        y[lenY - 1 - c] = (char)('0' + s.dy);
                    z[lenZ - 1 - c] = (char)('0' + s.dz);
                    carry = s.carry;
                    used = s.used;
                }
                return new String(x) + "+" + new String(y) + "=" + new String(z);
            }
        return "Impossible";
    }

    public static void main(String[] args) throws IOException {
        // the expression may be written with spaces, K comes last
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        List<String> tokens = new ArrayList<>();
        for (String line; (line = in.readLine()) != null;)
            for (String t : line.trim().split("\\s+"))
                if (!t.isEmpty())
                    tokens.add(t);
        StringBuilder text = new StringBuilder();
        for (int i = 0; i + 1 < tokens.size(); i++)
            text.append(tokens.get(i));
        System.out.println(solve(text.toString(), Integer.parseInt(tokens.get(tokens.size() - 1))));
    }
}
