import java.io.IOException;

public class Main {
    private static final int MAX_LENGTH = 300_000;
    private static final int TRIPLE_DIVISOR = 6;
    private static final int ODD_LENGTH_DIVISOR = 3;

    static long solve(byte[] word, int n) {
        if (n < 2) {
            return 0;
        }
        int i = 1;
        while (i < n && word[i] == word[0]) {
            i++;
        }
        if (i == n) {
            return (n + 1L) * n * (n - 1) / TRIPLE_DIVISOR;
        }
        if (word[0] != word[1]) {
            i = 2;
            while (i < n && word[i] == word[i - 2]) {
                i++;
            }
            if (i == n) {
                long half = n / 2;
                return n % 2 == 0 ? half * (half + 1) * (2 * half + 1) / TRIPLE_DIVISOR
                                  : half * (half + 1) * (half + 2) / ODD_LENGTH_DIVISOR;
            }
        }
        int[] radii = new int[n], ending = new int[n + 1], starting = new int[n + 1];
        int left = 0, right = -1;
        for (int center = 0; center < n; ++center) {
            int radius =
                center > right ? 1 : Math.min(radii[left + right - center], right - center + 1);
            while (center - radius >= 0 && center + radius < n &&
                   word[center - radius] == word[center + radius])
                ++radius;
            radii[center] = radius;
            if (center + radius - 1 > right) {
                left = center - radius + 1;
                right = center + radius - 1;
            }
            ++ending[center];
            --ending[center + radius];
            ++starting[center - radius + 1];
            --starting[center + 1];
        }
        left = 0;
        right = -1;
        for (int center = 0; center < n; ++center) {
            int radius =
                center > right ? 0 : Math.min(radii[left + right - center + 1], right - center + 1);
            while (center - radius - 1 >= 0 && center + radius < n &&
                   word[center - radius - 1] == word[center + radius])
                ++radius;
            radii[center] = radius;
            if (center + radius - 1 > right) {
                left = center - radius;
                right = center + radius - 1;
            }
            if (radius != 0) {
                ++ending[center];
                --ending[center + radius];
                ++starting[center - radius];
                --starting[center];
            }
        }
        int countEnding = 0, countStarting = starting[0];
        long answer = 0;
        for (int cut = 0; cut + 1 < n; ++cut) {
            countEnding += ending[cut];
            countStarting += starting[cut + 1];
            answer += (long)countEnding * countStarting;
        }
        return answer;
    }

    public static void main(String[] args) throws IOException {
        byte[] word = new byte[MAX_LENGTH + 2];
        int size = 0;
        while (size < word.length) {
            int count = System.in.read(word, size, word.length - size);
            if (count < 0) {
                break;
            }
            size += count;
        }
        while (size > 0 && word[size - 1] <= ' ') {
            size--;
        }
        System.out.println(solve(word, size));
    }
}
