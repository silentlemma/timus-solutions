import java.io.*;
import java.util.*;

public class Main {
    static final int NEVER = 1 << 30;
    static final int BOLT = -1, HEAL = 0; // spells; a teleport is its target square
    static int n, hpH, mpH, hpM, v, dH;
    static int[] bolt;
    static int[][][] need;

    // where the monsters stop after moving from square p
    static int land(int p) { return p - 1 < v ? 1 : p - v; }

    // the damage of a pack with h hit points that ends its move on p
    static int strike(int h, int p) { return p == 1 ? (h + hpM - 1) / hpM : 0; }

    // the hit points a spell needs with m mana against h hit points on p
    static int cost(int m, int h, int p, int spell) {
        int cure = 0;
        if (spell == BOLT) {
            if (h <= bolt[p])
                return 1;
            h -= bolt[p];
        } else if (spell == HEAL) {
            cure = dH;
        } else {
            p = spell;
        }
        int q = land(p), rest = need[m - 1][h][q];
        if (rest == NEVER)
            return NEVER;
        int req = strike(h, q) + rest;
        if (cure == 0)
            return req;
        return req > hpH ? NEVER : Math.max(1, req - cure);
    }

    static int next(StreamTokenizer in) throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        n = next(in);
        hpH = next(in);
        mpH = next(in);
        hpM = next(in);
        int nM = next(in);
        v = next(in);
        dH = next(in);
        bolt = new int[n + 1];
        for (int p = 1; p <= n; p++)
            bolt[p] = next(in);
        int top = nM * hpM;
        // need[m][h][p] is the fewest hit points the hero needs at the start of
        // a turn with m mana against a pack of h hit points on square p; more
        // hit points never hurt, so this number decides every state
        need = new int[mpH + 1][top + 1][n + 1];
        for (int[][] layer : need)
            for (int[] row : layer)
                Arrays.fill(row, NEVER);
        for (int m = 1; m <= mpH; m++)
            for (int h = 1; h <= top; h++)
                for (int p = 1; p <= n; p++) {
                    int best = NEVER;
                    for (int s = BOLT; s <= n; s++)
                        best = Math.min(best, cost(m, h, p, s));
                    need[m][h][p] = best;
                }
        int hp = hpH, h = top, p = n;
        if (need[mpH][h][p] > hp) {
            System.out.println("DEFEATED");
            return;
        }
        StringBuilder out = new StringBuilder("VICTORIOUS\n");
        // replay: any spell whose need the hero meets keeps the win in reach
        for (int m = mpH; h > 0; m--) {
            int s = BOLT;
            while (cost(m, h, p, s) > hp)
                s++;
            if (s == BOLT) {
                out.append("L\n");
                h -= bolt[p];
            } else if (s == HEAL) {
                out.append("H\n");
                hp = Math.min(hpH, hp + dH);
            } else {
                out.append("T ").append(s).append('\n');
                p = s;
            }
            if (h > 0) {
                p = land(p);
                hp -= strike(h, p);
            }
        }
        System.out.print(out);
    }
}
