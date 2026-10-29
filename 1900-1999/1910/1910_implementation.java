import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = in.nextInt();
        // try every section as the middle of the three
        int best = 0, middle = 0;
        for (int i = 1; i + 1 < n; i++) {
            int sum = a[i - 1] + a[i] + a[i + 1];
            if (sum > best) {
                best = sum;
                middle = i;
            }
        }
        System.out.println(best + " " + (middle + 1));
    }
}
