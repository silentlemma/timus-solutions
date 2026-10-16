import java.util.Scanner;

public class Main {
    static final int DISKS = 4, PETALS = 3, BITS = DISKS + PETALS;

    // petal j lies in every disk except disk j
    static boolean valid(int[] word) {
        int total = 0;
        for (int d = 0; d < DISKS; d++) total += word[d];
        for (int j = 0; j < PETALS; j++) {
            if ((total - word[j]) % 2 != word[DISKS + j]) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] word = new int[BITS];
        for (int i = 0; i < BITS; i++) word[i] = in.nextInt();
        // try the word as it is, then each single change
        for (int k = -1; k < BITS; k++) {
            if (k >= 0) word[k] ^= 1;
            if (valid(word)) break;
            if (k >= 0) word[k] ^= 1;
        }
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < BITS; i++) {
            if (i > 0) out.append(' ');
            out.append(word[i]);
        }
        System.out.println(out);
    }
}
