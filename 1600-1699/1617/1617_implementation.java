import java.util.*;

public class Main {
    static final int PAIRS_PER_CAR = 4;
    static final int LARGEST = 700; // the widest diameter in millimetres

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] count = new int[LARGEST + 1];
        for (int i = 0; i < n; i++)
            count[in.nextInt()]++;
        // each diameter equips as many cars as it has full sets of four pairs
        int cars = 0;
        for (int c : count)
            cars += c / PAIRS_PER_CAR;
        System.out.println(cars);
    }
}
