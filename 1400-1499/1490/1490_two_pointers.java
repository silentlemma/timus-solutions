import java.io.*;

public class Main {
    static final long QUARTERS = 4;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        long r = (long)in.nval;
        long y = r, total = 0, radiusSquared = r * r;
        // In column x, exactly y nearest corners lie strictly inside the disc.
        // The boundary moves down at most r times over the whole scan.
        for (long x = 0; x < r; x++) {
            while (y > 0 && x * x + (y - 1) * (y - 1) >= radiusSquared)
                y--;
            total += y;
        }
        System.out.println(QUARTERS * total);
    }
}
