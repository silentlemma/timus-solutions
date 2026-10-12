import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        long reach = next(in), rx = next(in), ry = next(in), lx = next(in), ly = next(in);
        long n = next(in);
        StringBuilder out = new StringBuilder();
        for (long i = 0; i < n; i++) {
            long x = next(in), y = next(in);
            // inside the sector means left of the right border and right of the
            // left one, borders included; the sector is narrower than a half turn
            long right = rx * y - ry * x, left = x * ly - y * lx;
            boolean inside = right >= 0 && left >= 0;
            // a border's extension behind the gun is out; for a sector of zero
            // width, both borders along one ray, no other test rejects it
            boolean behind =
                (right == 0 && rx * x + ry * y < 0) || (left == 0 && lx * x + ly * y < 0);
            out.append(inside && !behind && x * x + y * y <= reach * reach ? "YES\n" : "NO\n");
        }
        System.out.print(out);
    }

    static long next(StreamTokenizer in) throws IOException {
        in.nextToken();
        return (long)in.nval;
    }
}
