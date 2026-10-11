import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int x = in.nextInt(), y = in.nextInt();
        // each turn of the loop swaps x and y, and there are x + y turns; the
        // sum survives, so an odd sum of positive numbers means one swap
        if (x > 0 && y > 0 && (x + y) % 2 == 1) {
            int t = x;
            x = y;
            y = t;
        }
        System.out.println(x + " " + y);
    }
}
