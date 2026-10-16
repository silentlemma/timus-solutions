import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int l = in.nextInt(), k = in.nextInt(), h = in.nextInt();
        // the time to reach x is x h / k plus a part that repeats every k km
        // and lies between 0 and h, so the last l mod k km take 0 to h hours
        int whole = l / k, slowest = whole + (l % k > 0 ? 1 : 0);
        System.out.printf("%.8f %.8f%n", (double) whole * h, (double) slowest * h);
    }
}
