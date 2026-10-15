import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // Sandro's own spot holds no demon: stay there and reach the farthest one
        double farthest = 0;
        for (int i = 0; i < n; i++)
            farthest = Math.max(farthest, Math.hypot(in.nextInt(), in.nextInt()));
        System.out.println(String.format(Locale.US, "0 0 %.10f", farthest));
    }
}
