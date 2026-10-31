public class Main {
    static final String NAME = "Sandro";
    static final int COINS = 5;

    private static char lower(char c) {
        // the input contains only Latin letters.
        return c <= 'Z' ? (char)(c + ('a' - 'A')) : c;
    }

    public static void main(String[] args) throws java.io.IOException {
        // read the latin-letter token directly without scanner or regex allocation.
        StringBuilder text = new StringBuilder();
        int c;
        do {
            c = System.in.read();
        } while (c <= ' ' && c != -1);
        while (c > ' ') {
            text.append((char)c);
            c = System.in.read();
        }
        int best = Integer.MAX_VALUE;
        for (int start = 0; start + NAME.length() <= text.length(); start++) {
            int cost = 0;
            for (int k = 0; k < NAME.length(); k++) {
                char a = text.charAt(start + k), b = NAME.charAt(k);
                // one fee for the wrong case, one for the wrong letter
                if ((a <= 'Z') != (b <= 'Z'))
                    cost += COINS;
                if (lower(a) != lower(b))
                    cost += COINS;
            }
            best = Math.min(best, cost);
        }
        System.out.println(best);
    }
}
