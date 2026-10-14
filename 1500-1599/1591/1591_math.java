import java.util.*;

public class Main {
    static final int FOUR = 4; // one corner inside: 4 points, one triangle on each side
    static final int FIVE = 5; // two corners inside: 5 points, one triangle per apex
    static final int SIX = 6;  // three corners inside: 6 points, the three long diagonals

    static long choose(long n, int k) {
        long c = 1;
        for (int i = 1; i <= k; i++)
            c = c * (n - k + i) / i; // stays below C(n, k) * n
        return c;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        if (!in.hasNextLong())
            return;
        long n = in.nextLong();
        // a triangle is fixed by the set of chord ends it uses, and a set of
        // k points on the circle gives a fixed number of triangles
        System.out.println(choose(n, SIX) + FIVE * choose(n, FIVE) + FOUR * choose(n, FOUR));
    }
}
