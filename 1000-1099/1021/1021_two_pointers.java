import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int TARGET = 10000;
    static StreamTokenizer in =
        new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    static int[] readList() throws IOException {
        in.nextToken();
        int[] v = new int[(int)in.nval];
        for (int i = 0; i < v.length; i++) {
            in.nextToken();
            v[i] = (int)in.nval;
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        int[] up = readList(), down = readList();
        // up increases and down decreases: walking both forward, a sum that is
        // too small can only grow by moving in up, a sum too big only shrink in down
        int i = 0, j = 0;
        while (i < up.length && j < down.length && up[i] + down[j] != TARGET) {
            if (up[i] + down[j] < TARGET) {
                i++;
            } else {
                j++;
            }
        }
        System.out.println(i < up.length && j < down.length ? "YES" : "NO");
    }
}
