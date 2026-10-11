import java.io.*;

public class Main {
    static final int MANY = 2;

    static int next(StreamTokenizer in) throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int weight = next(in), n = next(in);
        int[] card = new int[n + 1];
        for (int i = 1; i <= n; i++)
            card[i] = next(in);
        // ways[i][s]: how many sets of the first i cards weigh s, counted up to 2
        byte[][] ways = new byte[n + 1][];
        ways[0] = new byte[weight + 1];
        ways[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            ways[i] = ways[i - 1].clone();
            for (int s = card[i]; s <= weight; s++)
                ways[i][s] = (byte)Math.min(MANY, ways[i][s] + ways[i - 1][s - card[i]]);
        }
        if (ways[n][weight] == 0) {
            System.out.println(0);
            return;
        }
        if (ways[n][weight] == MANY) {
            System.out.println(-1);
            return;
        }
        // the only set: card i is in it exactly when the rest cannot be made
        // from the cards before it
        boolean[] missing = new boolean[n + 1];
        for (int i = n, s = weight; i >= 1; i--) {
            if (ways[i - 1][s] == 1)
                missing[i] = true;
            else
                s -= card[i];
        }
        StringBuilder out = new StringBuilder();
        for (int i = 1; i <= n; i++)
            if (missing[i])
                out.append(out.length() > 0 ? " " : "").append(i);
        System.out.println(out);
    }
}
