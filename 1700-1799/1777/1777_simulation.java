import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        List<Long> piles = new ArrayList<>();
        while (in.hasNextLong()) piles.add(in.nextLong());
        int asked = 0;
        while (true) {
            asked++;
            // the closest two piles differ least among neighbours in sorted order
            Collections.sort(piles);
            long gap = Long.MAX_VALUE;
            for (int i = 1; i < piles.size(); i++) {
                gap = Math.min(gap, piles.get(i) - piles.get(i - 1));
            }
            if (gap == 0) break;
            piles.add(gap);
        }
        System.out.println(asked);
    }
}
