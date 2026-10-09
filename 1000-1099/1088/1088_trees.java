import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long d = in.nextLong(), e = in.nextLong(), f = in.nextLong();
        long dp = in.nextLong(), ep = in.nextLong(), h = in.nextLong();
        // pier p - 1 written in F bits is the path to it, a left turn being 1 and
        // the first turn the highest bit; a stone k hours from the sea is that
        // path without its last k turns
        long a = (ep - 1) >> e, depthA = f - e;
        long b = (dp - 1) >> d, depthB = f - d;
        long hours = 0;
        for (; depthA > depthB; depthA--, hours++) {
            a >>= 1;
        }
        for (; depthB > depthA; depthB--, hours++) {
            b >>= 1;
        }
        for (; a != b; hours += 2) {
            a >>= 1;
            b >>= 1;
        }
        System.out.println(hours <= h ? "YES" : "NO");
    }
}
