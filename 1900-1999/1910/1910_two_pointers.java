import java.util.Scanner;

public class Main {
    private static final int WINDOW_SIZE = 3;

    private static int[] maximumWindow(int[] values) {
        int current = 0;
        for (int index = 0; index < WINDOW_SIZE; index++) {
            current += values[index];
        }
        int best = current;
        int position = WINDOW_SIZE / 2 + 1;
        for (int start = 1; start + WINDOW_SIZE <= values.length; start++) {
            current += values[start + WINDOW_SIZE - 1] - values[start - 1];
            if (current > best) {
                best = current;
                position = start + WINDOW_SIZE / 2 + 1;
            }
        }
        return new int[] {best, position};
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int count = in.nextInt();
        int[] values = new int[count];
        for (int index = 0; index < count; index++) {
            values[index] = in.nextInt();
        }
        int[] answer = maximumWindow(values);
        System.out.println(answer[0] + " " + answer[1]);
    }
}
