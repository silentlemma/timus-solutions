import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static final int MOST = 30;

    // compares (total, away goals) pairs
    static boolean atLeast(int a1, int a2, int b1, int b2) {
        return a1 > b1 || a1 == b1 && a2 >= b2;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine().trim());
        StringBuilder out = new StringBuilder();
        for (int test = 0; test < t; test++) {
            String line = in.readLine();
            List<Integer> numbers = new ArrayList<>();
            for (String word : line.trim().split("\\s+")) {
                if (word.matches("\\d+")) numbers.add(Integer.parseInt(word));
            }
            boolean firstHome = line.contains(" home ");
            int x = numbers.get(0), y = numbers.get(1), lowest = -1, highest = -1;
            for (int g = 0; g <= MOST; g++) {
                boolean canPass = false, canFail = false;
                for (int o = 0; o <= MOST; o++) {
                    // totals first, then goals scored at the other team's
                    // stadium; equal on both counts: a coin decides
                    int oursAway = firstHome ? g : x, theirsAway = firstHome ? y : o;
                    if (atLeast(x + g, oursAway, y + o, theirsAway)) canPass = true;
                    if (atLeast(y + o, theirsAway, x + g, oursAway)) canFail = true;
                }
                if (canPass && lowest == -1) lowest = g;
                if (canFail) highest = g;
            }
            out.append(lowest).append(' ').append(highest).append('\n');
        }
        System.out.print(out);
    }
}
