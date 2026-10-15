import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long m = in.nextLong(), n = in.nextLong();
        // m * n moves close the tour; m + n + 1 of them are diagonal
        long diagonal = m + n + 1;
        double length = m * n + diagonal * (Math.sqrt(2) - 1);
        System.out.println(String.format(Locale.US, "%.12f", length));
    }
}
