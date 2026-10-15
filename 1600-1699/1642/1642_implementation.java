import java.util.*;

public class Main {
    static final int FAR = 2000; // beyond every coordinate

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), x = in.nextInt();
        // the nearest obstacles on both sides; walking away from the exit is
        // promised to meet one, so the one needed below always exists
        int left = -FAR, right = FAR;
        for (int i = 0; i < n; i++) {
            int w = in.nextInt();
            if (w < 0)
                left = Math.max(left, w);
            else
                right = Math.min(right, w);
        }
        if (x < left || x > right)
            System.out.println("Impossible"); // an obstacle stands between the start and the exit
        else if (x > 0)
            System.out.println(x + " " + (-2 * left + x));
        else
            System.out.println((2 * right - x) + " " + (-x));
    }
}
