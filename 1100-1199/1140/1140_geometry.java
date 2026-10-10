import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        long sx = 0, sy = 0, sz = 0;
        for (int k = 0; k < n; k++) {
            in.nextToken();
            char d = in.sval.charAt(0);
            in.nextToken();
            long len = (long)in.nval;
            if (d == 'X') {
                sx += len;
            } else if (d == 'Y') {
                sy += len;
            } else {
                sz += len;
            }
        }
        // a step along Y is a step along X and one along Z, so the walk ends
        // at a X + b Z; going back with m steps along Y costs |a - m| + |m| +
        // |b - m|, which is smallest at the median of a, 0 and b
        long a = sx + sy, b = sz + sy;
        long m = Math.max(Math.min(a, b), Math.min(Math.max(a, b), 0));
        char[] dirs = {'X', 'Y', 'Z'};
        long[] lens = {m - a, -m, m - b};
        StringBuilder body = new StringBuilder();
        int count = 0;
        for (int k = 0; k < dirs.length; k++) {
            if (lens[k] != 0) {
                body.append(dirs[k]).append(' ').append(lens[k]).append('\n');
                count++;
            }
        }
        System.out.print(count + "\n" + body);
    }
}
