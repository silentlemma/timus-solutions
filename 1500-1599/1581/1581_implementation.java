import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++)
            numbers[i] = in.nextInt();
        // each run of equal numbers is said as its length and then the number
        StringJoiner out = new StringJoiner(" ");
        for (int i = 0; i < n;) {
            int j = i;
            while (j < n && numbers[j] == numbers[i])
                j++;
            out.add(String.valueOf(j - i)).add(String.valueOf(numbers[i]));
            i = j;
        }
        System.out.println(out);
    }
}
