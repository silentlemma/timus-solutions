import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int k = in.nextInt();
        int[] size = new int[k];
        for (int i = 0; i < k; i++) {
            size[i] = in.nextInt();
        }
        // win a majority of the groups, choosing the smallest ones; a group of s
        // voters needs s / 2 + 1 supporters
        Arrays.sort(size);
        int supporters = 0;
        for (int i = 0; i <= k / 2; i++) {
            supporters += size[i] / 2 + 1;
        }
        System.out.println(supporters);
    }
}
