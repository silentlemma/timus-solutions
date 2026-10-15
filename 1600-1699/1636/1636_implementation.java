import java.util.*;

public class Main {
    static final int PROBLEMS = 10;
    static final int PER_ATTEMPT = 20; // minutes for each rejected attempt

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t1 = in.nextInt(), t2 = in.nextInt();
        int clean = t2;
        for (int i = 0; i < PROBLEMS; i++)
            clean -= PER_ATTEMPT * in.nextInt();
        // without the rejected attempts ZZZ wins only with strictly less time
        System.out.println(clean < t1 ? "Dirty debug :(" : "No chance.");
    }
}
