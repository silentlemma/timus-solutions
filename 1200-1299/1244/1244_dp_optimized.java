import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int MANY = 2;

    static int next(StreamTokenizer input) throws Exception {
        input.nextToken();
        return (int)input.nval;
    }

    public static void main(String[] args) throws Exception {
        StreamTokenizer input =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int weight = next(input), n = next(input), total = 0;
        int[] cards = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            cards[i] = next(input);
            total += cards[i];
        }
        boolean selectMissing = total - weight < weight;
        int target = Math.min(weight, total - weight);
        byte[] ways = new byte[target + 1], last = new byte[target + 1];
        ways[0] = 1;
        // Complementing subsets preserves uniqueness. Descending sums avoid
        // reusing a card, and first-reach parents never change afterwards.
        for (int i = 1; i <= n; i++) {
            for (int sum = target; sum >= cards[i]; sum--) {
                if (ways[sum] == 0 && ways[sum - cards[i]] != 0)
                    last[sum] = (byte)i;
                ways[sum] = (byte)Math.min(MANY, ways[sum] + ways[sum - cards[i]]);
            }
            if (ways[target] == MANY) {
                System.out.println(-1);
                return;
            }
        }
        if (ways[target] == 0) {
            System.out.println(0);
            return;
        }
        boolean[] chosen = new boolean[n + 1];
        for (int sum = target; sum > 0; sum -= cards[last[sum]])
            chosen[last[sum]] = true;
        StringBuilder output = new StringBuilder();
        for (int i = 1; i <= n; i++)
            if (chosen[i] == selectMissing) {
                if (output.length() > 0)
                    output.append(' ');
                output.append(i);
            }
        System.out.println(output);
    }
}
