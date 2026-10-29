public class Main {
    private static final int SIZE = 4;

    // the squares are read character by character from System.in
    private static byte nextCharacter() throws java.io.IOException {
        int ch;
        do {
            ch = System.in.read();
        } while (ch != -1 && ch <= ' ');
        return (byte)ch;
    }

    public static void main(String[] args) throws java.io.IOException {
        byte[][] grille = new byte[SIZE][SIZE];
        byte[][] square = new byte[SIZE][SIZE];
        byte[][] turned = new byte[SIZE][SIZE];
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++)
                grille[r][c] = nextCharacter();
        }
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++)
                square[r][c] = nextCharacter();
        }
        // the password goes out as one byte array, without a String
        byte[] password = new byte[SIZE * SIZE + 1];
        int length = 0;
        // read the windows row by row, then turn the grille clockwise:
        // the cell (r, c) of the turned grille is (SIZE - 1 - c, r) of the old one
        for (int turn = 0; turn < SIZE; turn++) {
            for (int r = 0; r < SIZE; r++) {
                for (int c = 0; c < SIZE; c++) {
                    if (grille[r][c] == 'X')
                        password[length++] = square[r][c];
                }
            }
            for (int r = 0; r < SIZE; r++) {
                for (int c = 0; c < SIZE; c++)
                    turned[r][c] = grille[SIZE - 1 - c][r];
            }
            // the two arrays swap roles, so no new array is made for a turn
            byte[][] previous = grille;
            grille = turned;
            turned = previous;
        }
        password[length++] = '\n';
        System.out.write(password, 0, length);
    }
}
