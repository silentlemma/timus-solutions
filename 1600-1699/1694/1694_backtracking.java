import java.util.Scanner;

public class Main {
    static int k;
    static int longest;
    static int[] word;
    static int size;
    static long[][] counts;

    // whether some k-repetition ends at the last letter of word
    static boolean repetitionAtEnd() {
        for (int block = 1; block * k <= size; block++) {
            int i = size - k * block;
            while (i < size - block && word[i] == word[i + block]) {
                i++;
            }
            if (i == size - block) {
                return true;
            }
        }
        return false;
    }

    // whether w^k has a k-repetition other than itself; w has none, and w^k
    // repeats with period |w|, so only windows that start in the first copy
    // and leave it need a look
    static boolean properRepetition() {
        int total = size * k;
        for (int block = 1; block <= size; block++) {
            int span = k * block;
            for (int start = 0; start < size && start <= total - span; start++) {
                if (start + span <= size || span == total) {
                    continue;
                }
                int i = start;
                int end = start + span - block;
                while (i < end && word[i % size] == word[(i + block) % size]) {
                    i++;
                }
                if (i == end) {
                    return true;
                }
            }
        }
        return false;
    }

    static void extend(int distinct) {
        // w^k may fail while a longer w still works, so this only skips counting
        if (size > 0 && !properRepetition()) {
            counts[size][distinct]++;
        }
        if (size == longest) {
            return;
        }
        for (int c = 0; c <= distinct; c++) {
            word[size++] = c;
            // a k-repetition inside w is one inside the killer word too
            if (!repetitionAtEnd()) {
                extend(Math.max(distinct, c + 1));
            }
            size--;
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m = in.nextInt();
        k = in.nextInt();
        int n = in.nextInt();
        // a killer word is w repeated k times; whether it works does not depend
        // on which letters w uses, so count the words w with letters numbered in
        // order of first appearance, by their number of different letters
        longest = n / k;
        word = new int[longest + 1];
        counts = new long[longest + 1][longest + 1];
        extend(0);
        long total = 0;
        for (int length = 1; length <= longest; length++) {
            long ways = 1;
            for (int distinct = 1; distinct <= length; distinct++) {
                ways *= Math.max(m - distinct + 1, 0);
                total += counts[length][distinct] * ways;
            }
        }
        System.out.println(total);
    }
}
