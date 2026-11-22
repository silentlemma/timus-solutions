public class Main {
    static final int SIDE = 3, CELLS = SIDE * SIDE, ALL = (1 << CELLS) - 1;
    static final int ROW = (1 << SIDE) - 1;
    static final int COLUMN = 1 | (1 << SIDE) | (1 << (2 * SIDE));
    static final int DIAGONAL = 1 | (1 << (SIDE + 1)) | (1 << (2 * (SIDE + 1)));
    static final int ANTIDIAGONAL =
        (1 << (SIDE - 1)) | (1 << (2 * (SIDE - 1))) | (1 << (SIDE * (SIDE - 1)));
    static final int WIN = 1, DRAW = 0, LOSS = -1, BUFFER_SIZE = 64, BYTE_MASK = 255;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0)
                return -1;
        }
        return buffer[position++] & BYTE_MASK;
    }

    static boolean won(int mask) {
        for (int i = 0; i < SIDE; i++) {
            int row = ROW << (i * SIDE), column = COLUMN << i;
            if ((mask & row) == row || (mask & column) == column)
                return true;
        }
        return (mask & DIAGONAL) == DIAGONAL || (mask & ANTIDIAGONAL) == ANTIDIAGONAL;
    }

    static int play(int own, int other) {
        int free = ALL ^ (own | other), best = free == 0 ? DRAW : LOSS;
        while (free != 0) {
            int bit = free & -free;
            free ^= bit;
            int result = won(own | bit) ? WIN : -play(other, own | bit);
            if (result == WIN)
                return WIN;
            if (result > best)
                best = result;
        }
        return best;
    }

    public static void main(String[] args) throws java.io.IOException {
        int crosses = 0, noughts = 0;
        for (int i = 0; i < CELLS; i++) {
            int c = read();
            while (c >= 0 && c <= ' ')
                c = read();
            if (c == 'X')
                crosses |= 1 << i;
            else if (c == 'O')
                noughts |= 1 << i;
        }
        // Exactly three cells are empty: the same short minimax needs no memo table.
        int result = play(crosses, noughts);
        System.out.println(result == WIN ? "Crosses win" : result == DRAW ? "Draw" : "Ouths win");
    }
}
