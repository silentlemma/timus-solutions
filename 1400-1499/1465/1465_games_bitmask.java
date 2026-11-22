public class Main {
    static final int PERIOD = 34;
    static final int FIRST_EXCEPTION = 14;
    static final int SECOND_EXCEPTION = 34;
    // 1465_games_bitmask_table.py finds losing residues 4, 8, 20, 24 and 28.
    static final long LOSING_RESIDUES = 0x11100110L;

    public static void main(String[] args) throws Exception {
        int digit = System.in.read();
        while (digit >= 0 && digit <= ' ')
            digit = System.in.read();
        if (digit == '+')
            digit = System.in.read();
        int columns = 0;
        while (digit >= '0' && digit <= '9') {
            columns = columns * 10 + (digit - '0');
            digit = System.in.read();
        }
        // In the finite prefix only lengths 14 and 34 lose outside the periodic residues.
        boolean loses = columns == FIRST_EXCEPTION || columns == SECOND_EXCEPTION ||
                        ((LOSING_RESIDUES >>> (columns % PERIOD)) & 1) != 0;
        System.out.println(loses ? "Black" : "White");
    }
}
