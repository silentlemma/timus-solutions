import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int gap = in.nextInt(), n = in.nextInt();
        // at a stop with trams every k minutes the officer, arriving gap
        // minutes after the thief, leaves at best gap - gap % k minutes later,
        // and a gap below k means the thief may still be waiting there
        for (int i = 0; i < n; i++) {
            int k = in.nextInt();
            gap -= gap % k;
            if (gap == 0) {
                System.out.println("YES");
                return;
            }
        }
        System.out.println("NO");
    }
}
