import java.util.Scanner;

public class Main {
    static final String NAME = "Sandro";
    static final int COINS = 5;

    public static void main(String[] args) {
        String text = new Scanner(System.in).next();
        int best = Integer.MAX_VALUE;
        for (int start = 0; start + NAME.length() <= text.length(); start++) {
            int cost = 0;
            for (int k = 0; k < NAME.length(); k++) {
                char a = text.charAt(start + k), b = NAME.charAt(k);
                // one fee for the wrong case, one for the wrong letter
                if (Character.isUpperCase(a) != Character.isUpperCase(b)) cost += COINS;
                if (Character.toLowerCase(a) != Character.toLowerCase(b)) cost += COINS;
            }
            best = Math.min(best, cost);
        }
        System.out.println(best);
    }
}
