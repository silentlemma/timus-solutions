import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    static final int PILES = 4, RANKS = 13;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        char[][] suits = new char[PILES][RANKS];
        for (int i = 0; i < PILES; i++) {
            for (int j = 0; j < RANKS; j++) {
                String card = in.next();
                suits[i][j] = card.charAt(card.length() - 1);
            }
        }
        int moves = 0;
        for (int level = 0; level + 1 < RANKS; level++) {
            // once the cards above level j sit in one-suit runs, the run ending at
            // level j of pile i must go onto the card one rank lower in its suit,
            // which lies at level j + 1 of pile target[i]
            Map<Character, Integer> holder = new HashMap<>();
            for (int k = 0; k < PILES; k++) holder.put(suits[k][level + 1], k);
            int[] target = new int[PILES];
            for (int i = 0; i < PILES; i++) target[i] = holder.get(suits[i][level]);
            // every pile with a change of suit here needs one move, and each cycle
            // of such piles needs one more, to a new pile and back
            boolean[] seen = new boolean[PILES];
            for (int i = 0; i < PILES; i++) {
                if (target[i] == i || seen[i]) continue;
                moves++;
                for (int k = i; !seen[k]; k = target[k]) {
                    seen[k] = true;
                    moves++;
                }
            }
        }
        System.out.println(moves);
    }
}
