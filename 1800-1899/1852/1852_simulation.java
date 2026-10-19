import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    static final String NAMES = "UDLRFB";
    // the outward normal of every face, in the order of NAMES
    static final int[][] FACES = {
        {0, 1, 0}, {0, -1, 0}, {-1, 0, 0}, {1, 0, 0}, {0, 0, 1}, {0, 0, -1}
    };

    static int dot(int[] a, int[] b) {
        int s = 0;
        for (int k = 0; k < a.length; k++) {
            s += a[k] * b[k];
        }
        return s;
    }

    // a quarter turn of v about the axis a: counter-clockwise seen from the
    // tip of a for sign 1, clockwise for sign -1
    static int[] turn(int[] v, int[] a, int sign) {
        int[] cross = {
            a[1] * v[2] - a[2] * v[1], a[2] * v[0] - a[0] * v[2], a[0] * v[1] - a[1] * v[0]
        };
        int along = dot(a, v);
        int[] r = new int[a.length];
        for (int k = 0; k < r.length; k++) {
            r[k] = sign * cross[k] + a[k] * along;
        }
        return r;
    }

    static long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        String moves = new BufferedReader(new InputStreamReader(System.in)).readLine().trim();
        // a sticker is a cubie position with every coordinate in -1..1 and
        // the outward normal of a face that cubie touches, as a key string
        List<int[][]> stickers = new ArrayList<>();
        Map<String, Integer> index = new HashMap<>();
        for (int x = -1; x <= 1; x++) {
            for (int y = -1; y <= 1; y++) {
                for (int z = -1; z <= 1; z++) {
                    int[] p = {x, y, z};
                    for (int[] n : FACES) {
                        if (dot(p, n) == 1) {
                            index.put(Arrays.toString(p) + Arrays.toString(n), stickers.size());
                            stickers.add(new int[][] {p, n});
                        }
                    }
                }
            }
        }
        int count = stickers.size();
        // the place every sticker moves to under each letter
        int[][] table = new int[Character.MAX_VALUE + 1][];
        for (int f = 0; f < FACES.length; f++) {
            int[] a = FACES[f];
            for (int sign : new int[] {1, -1}) {
                char letter = NAMES.charAt(f);
                if (sign == -1) {
                    letter = Character.toLowerCase(letter);
                }
                int[] to = new int[count];
                for (int i = 0; i < count; i++) {
                    int[] p = stickers.get(i)[0];
                    int[] n = stickers.get(i)[1];
                    to[i] = i;
                    if (dot(p, a) == 1) {
                        String key = Arrays.toString(turn(p, a, sign))
                                + Arrays.toString(turn(n, a, sign));
                        to[i] = index.get(key);
                    }
                }
                table[letter] = to;
            }
        }
        // where each sticker ends up after the whole sequence
        int[] place = new int[count];
        for (int i = 0; i < count; i++) {
            place[i] = i;
        }
        for (int c = 0; c < moves.length(); c++) {
            int[] to = table[moves.charAt(c)];
            for (int j = 0; j < count; j++) {
                place[j] = to[place[j]];
            }
        }
        // the sequence returns the cube after the lcm of the cycle lengths
        long order = 1;
        boolean[] seen = new boolean[count];
        for (int start = 0; start < count; start++) {
            long length = 0;
            for (int i = start; !seen[i]; i = place[i]) {
                seen[i] = true;
                length++;
            }
            if (length > 0) {
                order = order / gcd(order, length) * length;
            }
        }
        System.out.println(order - 1);
    }
}
