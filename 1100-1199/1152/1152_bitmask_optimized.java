import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static int[] monsters, volleys;
    static final int INITIAL_CAPACITY = 16;
    static final int HASH_MULTIPLIER = 0x9e3779b9;
    static final int HASH_ROTATION = 16;
    static int[] keys = new int[INITIAL_CAPACITY], costs = new int[INITIAL_CAPACITY];
    static int used;

    // primitive open addressing avoids boxing; wrapping multiplication mixes mask bits.
    static int slot(int key) {
        int index = Integer.rotateLeft(key * HASH_MULTIPLIER, HASH_ROTATION) & (keys.length - 1);
        while (keys[index] != 0 && keys[index] != key)
            index = (index + 1) & (keys.length - 1);
        return index;
    }

    static void save(int key, int cost) {
        if (2 * used == keys.length) {
            int[] oldKeys = keys, oldCosts = costs;
            keys = new int[2 * keys.length];
            costs = new int[keys.length];
            for (int i = 0; i < oldKeys.length; i++) {
                if (oldKeys[i] == 0)
                    continue;
                int index = slot(oldKeys[i]);
                keys[index] = oldKeys[i];
                costs[index] = oldCosts[i];
            }
        }
        int index = slot(key);
        keys[index] = key;
        costs[index] = cost;
        used++;
    }

    // store only reachable masks, with the living sum included in each cost.
    static int damage(int mask) {
        if (mask == 0)
            return 0;
        int index = slot(mask);
        if (keys[index] != 0)
            return costs[index];
        int best = -1, sum = 0;
        for (int i = 0; i < monsters.length; i++) {
            if ((mask >> i & 1) != 0)
                sum += monsters[i];
            int rest = mask & ~volleys[i];
            if (rest != mask) {
                int cost = damage(rest);
                if (best < 0 || cost < best)
                    best = cost;
            }
        }
        save(mask, best + sum);
        return best + sum;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval, total = 0;
        monsters = new int[n];
        volleys = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            monsters[i] = (int)in.nval;
            total += monsters[i];
            volleys[i] = 1 << ((i + n - 1) % n) | 1 << i | 1 << ((i + 1) % n);
        }
        System.out.println(damage((1 << n) - 1) - total);
    }
}
