import java.util.*;

public class Main {
    static final int KNOWN_HUNGRY = 2, KNOWN_FULL = 10; // given in the statement

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int hungry = KNOWN_HUNGRY, full = KNOWN_FULL;
        for (int i = 0; i < n; i++) {
            int count = in.nextInt();
            if (in.next().equals("hungry"))
                hungry = Math.max(hungry, count);
            else
                full = Math.min(full, count);
        }
        // the smallest satisfying amount must exceed the largest hungry one
        System.out.println(full > hungry ? String.valueOf(full) : "Inconsistent");
    }
}
