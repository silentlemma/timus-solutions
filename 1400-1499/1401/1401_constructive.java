import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.Scanner;

public class Main {
    static class Square {
        final int top, left, side, holeRow, holeCol;

        Square(int top, int left, int side, int holeRow, int holeCol) {
            this.top = top;
            this.left = left;
            this.side = side;
            this.holeRow = holeRow;
            this.holeCol = holeCol;
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), x = in.nextInt(), y = in.nextInt();
        int size = 1 << n, count = 0;
        int[][] board = new int[size][size];
        // each square has one cell that is already taken: the hole or a piece
        // of the tromino in the middle of the square above it
        ArrayDeque<Square> stack = new ArrayDeque<>();
        stack.push(new Square(0, 0, size, x - 1, y - 1));
        while (!stack.isEmpty()) {
            Square s = stack.pop();
            if (s.side == 1)
                continue;
            int half = s.side / 2;
            count++;
            for (int dr = 0; dr < 2; dr++)
                for (int dc = 0; dc < 2; dc++) {
                    int r0 = s.top + dr * half, c0 = s.left + dc * half;
                    if (r0 <= s.holeRow && s.holeRow < r0 + half && c0 <= s.holeCol &&
                        s.holeCol < c0 + half)
                        stack.push(new Square(r0, c0, half, s.holeRow, s.holeCol));
                    else {
                        // the cell of this quarter next to the middle of the square
                        int r = s.top + half - 1 + dr, c = s.left + half - 1 + dc;
                        board[r][c] = count;
                        stack.push(new Square(r0, c0, half, r, c));
                    }
                }
        }
        StringBuilder out = new StringBuilder();
        for (int[] row : board)
            for (int c = 0; c < size; c++)
                out.append(row[c]).append(c + 1 < size ? ' ' : '\n');
        PrintWriter pw = new PrintWriter(System.out);
        pw.print(out);
        pw.flush();
    }
}
