import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long k = in.nextLong(), p = in.nextLong();
        // an ent with w words teaches an old ent who ends with w + 1 words and a
        // young one who ends with 2w, so with g(m) ents knowing 2m (or 2m + 1)
        // words: g(1) = 1 and g(m) = g(m - 1) + g(m / 2)
        if (k < 2) {
            System.out.println(0);
            return;
        }
        int top = (int)(k / 2), half = top / 2; // only g up to half is looked up again
        int[] g = new int[half + 1];
        long cur = 1 % p;
        if (half >= 1)
            g[1] = (int)cur;
        for (int m = 2; m <= top; m++) {
            cur = (cur + g[m / 2]) % p;
            if (m <= half)
                g[m] = (int)cur;
        }
        System.out.println(cur);
    }
}
