import java.util.Scanner;

public class Main {
    // contests played by players 0 to 13, counted from the story
    static final int[] CONTESTS = {5, 21, 12, 2, 1, 4, 6, 1, 4, 4, 1, 0, 1, 1};

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println(CONTESTS[in.nextInt()]);
    }
}
