import java.io.*;

public class Main {
    static final int INPUT_VALUES = 6;

    static int index(int n, int m, int r, int c) {
        int layer = Math.min(Math.min(r, c), Math.min(n - 1 - r, m - 1 - c));
        int height = n - 2 * layer, width = m - 2 * layer;
        r -= layer;
        c -= layer;
        // Outer layers contain the cells outside this remaining rectangle.
        int before = n * m - height * width, offset;
        if (height == 1)
            offset = c;
        else if (width == 1)
            offset = r;
        else if (r == 0)
            offset = c;
        else if (c == width - 1)
            offset = width - 1 + r;
        else if (r == height - 1)
            offset = width - 1 + height - 1 + width - 1 - c;
        else
            offset = 2 * (height + width - 2) - r;
        return before + offset;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int[] v = new int[INPUT_VALUES];
        for (int i = 0; i < v.length; i++) {
            in.nextToken();
            v[i] = (int)in.nval;
        }
        int p = 0, n = v[p++], m = v[p++], r1 = v[p++] - 1, c1 = v[p++] - 1;
        int r2 = v[p++] - 1, c2 = v[p] - 1;
        System.out.println(Math.abs(index(n, m, r1, c1) - index(n, m, r2, c2)));
    }
}
