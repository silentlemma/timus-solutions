import java.util.*;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // rows of the ages 1..k starting with 1: a(k) = a(k-1) + a(k-3) + 1,
        // with a(1) = 1 and the rule run back to a(0) = 0, a(-1) = -1
        long older = -1, old = 0, cur = 1;
        for (int i = 1; i < n; i++) {
            long next = cur + older + 1;
            older = old;
            old = cur;
            cur = next;
        }
        System.out.println(cur);
    }
}
