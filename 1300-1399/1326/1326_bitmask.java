import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));

    static int next() throws IOException {
        return in.nextToken() == StreamTokenizer.TT_EOF ? 0 : (int)in.nval;
    }

    public static void main(String[] args) throws IOException {
        int n = next();
        List<int[]> offers = new ArrayList<>(); // a price and the caps as a mask over 1..n
        for (int i = 0; i < n; i++)
            offers.add(new int[] {next(), 1 << i});
        int m = next();
        for (int j = 0; j < m; j++) {
            int price = next(), size = next(), mask = 0;
            for (int k = 0; k < size; k++)
                mask |= 1 << (next() - 1);
            offers.add(new int[] {price, mask});
        }
        int count = next();
        // the wanted caps get the bits 0, 1, ... of a smaller mask
        int[] bit = new int[n];
        int wanted = 0;
        for (int k = 0; k < count; k++) {
            int cap = next() - 1;
            if (bit[cap] == 0)
                bit[cap] = 1 << wanted++;
        }
        int full = (1 << wanted) - 1;
        // offers that hold each wanted cap, as a price and the bits they leave
        List<List<int[]>> byLow = new ArrayList<>();
        for (int i = 0; i < wanted; i++)
            byLow.add(new ArrayList<>());
        for (int[] offer : offers) {
            int mask = 0;
            for (int i = 0; i < n; i++) {
                if ((offer[1] >> i & 1) == 1)
                    mask |= bit[i];
            }
            for (int i = 0; i < wanted; i++) {
                if ((mask >> i & 1) == 1)
                    byLow.get(i).add(new int[] {offer[0], full & ~mask});
            }
        }
        int[][] prices = new int[wanted][], keeps = new int[wanted][];
        for (int i = 0; i < wanted; i++) {
            List<int[]> list = byLow.get(i);
            prices[i] = new int[list.size()];
            keeps[i] = new int[list.size()];
            for (int k = 0; k < list.size(); k++) {
                prices[i][k] = list.get(k)[0];
                keeps[i][k] = list.get(k)[1];
            }
        }
        // cheapest[s]: the least money that buys every cap of the set s; some
        // offer must hold its lowest cap
        int[] cheapest = new int[full + 1];
        for (int s = 1; s <= full; s++) {
            int low = Integer.numberOfTrailingZeros(s), least = Integer.MAX_VALUE;
            int[] price = prices[low], keep = keeps[low];
            for (int k = 0; k < price.length; k++)
                least = Math.min(least, price[k] + cheapest[s & keep[k]]);
            cheapest[s] = least;
        }
        System.out.println(cheapest[full]);
    }
}
