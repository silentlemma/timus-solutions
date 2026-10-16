import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long ax = in.nextLong(), ay = in.nextLong(), bx = in.nextLong(), by = in.nextLong();
        long cx = in.nextLong(), cy = in.nextLong(), dx = in.nextLong(), dy = in.nextLong();
        // both walks stay in the boxes of their ends, so the shared part lies in
        // the overlap of the two boxes
        long width = Math.min(Math.max(ax, bx), Math.max(cx, dx))
                - Math.max(Math.min(ax, bx), Math.min(cx, dx));
        long height = Math.min(Math.max(ay, by), Math.max(cy, dy))
                - Math.max(Math.min(ay, by), Math.min(cy, dy));
        if (width < 0 || height < 0) {
            System.out.println(0);
            return;
        }
        // walks rising the same way can share a staircase across the overlap, while
        // one rising and one falling share only one straight piece
        long first = Long.signum(bx - ax) * Long.signum(by - ay);
        long second = Long.signum(dx - cx) * Long.signum(dy - cy);
        System.out.println(first * second < 0 ? Math.max(width, height) : width + height);
    }
}
