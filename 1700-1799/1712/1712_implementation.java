import java.util.Scanner;

public class Main {
    static final int SIZE = 4;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        char[][] grille = new char[SIZE][];
        char[][] square = new char[SIZE][];
        for (int r = 0; r < SIZE; r++) {
            grille[r] = in.next().toCharArray();
        }
        for (int r = 0; r < SIZE; r++) {
            square[r] = in.next().toCharArray();
        }
        StringBuilder password = new StringBuilder();
        // read the windows row by row, then turn the grille clockwise:
        // the cell (r, c) of the turned grille is (SIZE - 1 - c, r) of the old one
        for (int turn = 0; turn < SIZE; turn++) {
            for (int r = 0; r < SIZE; r++) {
                for (int c = 0; c < SIZE; c++) {
                    if (grille[r][c] == 'X') {
                        password.append(square[r][c]);
                    }
                }
            }
            char[][] turned = new char[SIZE][SIZE];
            for (int r = 0; r < SIZE; r++) {
                for (int c = 0; c < SIZE; c++) {
                    turned[r][c] = grille[SIZE - 1 - c][r];
                }
            }
            grille = turned;
        }
        System.out.println(password);
    }
}
