import java.util.*;

public class Main {
    static final int FREE = 6; // calls of up to six seconds cost nothing
    static final int MINUTE = 60;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n1 = in.nextLong(), c1 = in.nextLong();
        long n2 = in.nextLong(), t = in.nextLong(), c2 = in.nextLong();
        long n3 = in.nextLong();
        int k = in.nextInt();
        long minutes = 0;
        for (int i = 0; i < k; i++) {
            String[] parts = in.next().split(":");
            int seconds = Integer.parseInt(parts[0]) * MINUTE + Integer.parseInt(parts[1]);
            if (seconds > FREE)
                minutes += (seconds + MINUTE - 1) / MINUTE; // a started minute counts in full
        }
        System.out.println("Basic:     " + (n1 + c1 * minutes));
        System.out.println("Combined:  " + (n2 + c2 * Math.max(0, minutes - t)));
        System.out.println("Unlimited: " + n3);
    }
}
