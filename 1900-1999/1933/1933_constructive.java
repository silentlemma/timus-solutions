import java.util.Scanner;

public class Main {
    static int[][] buildSchedule(int cannons) {
        int size = 2 * cannons + 1;
        int[][] schedule = new int[size][size];
        for (int row = 0; row < size; row++) {
            for (int column = 0; column < size; column++) {
                if (row != column) {
                    schedule[row][column] = (row + column + size - 1) % size + 1;
                }
            }
        }
        return schedule;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int cannons = input.nextInt();
        StringBuilder output = new StringBuilder();
        for (int[] row : buildSchedule(cannons)) {
            for (int column = 0; column < row.length; column++) {
                if (column > 0) {
                    output.append(' ');
                }
                output.append(row[column]);
            }
            output.append('\n');
        }
        System.out.print(output);
    }
}
