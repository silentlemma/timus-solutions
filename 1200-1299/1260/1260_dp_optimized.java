import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        // a single small integer needs no scanner or token allocations.
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        int n = 0;
        while (c >= '0' && c <= '9') {
            n = n * 10 + c - '0';
            c = System.in.read();
        }
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
