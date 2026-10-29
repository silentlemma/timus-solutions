import java.util.Scanner;

public class Main {
    static final int TARGET = 6;
    static final int KINDS = 3;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] counts = new int[KINDS];
        // ways is the number of different words from the pieces read so far
        int ways = 1;
        boolean enough = false;
        for (int length = 1; length <= n; length++) {
            int letter = in.nextInt() - 1;
            counts[letter]++;
            ways = ways * length / counts[letter];
            if (ways >= TARGET) {
                enough = true;
                break;
            }
        }
        System.out.println(enough ? "Yes" : "No");
    }
}
