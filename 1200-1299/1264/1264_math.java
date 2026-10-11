import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong(), m = in.nextLong();
        // one line for each element and each value 0..M
        System.out.println(n * (m + 1));
    }
}
