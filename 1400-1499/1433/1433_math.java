public class Main {
    static final int FACES = 4, LETTERS = 26;

    static boolean equivalent(char[] a, char[] b) {
        int[] count = new int[LETTERS];
        int seen = 0;
        boolean duplicate = false;
        for (int i = 0; i < FACES; i++) {
            count[a[i] - 'A']++;
            count[b[i] - 'A']--;
            int bit = 1 << (a[i] - 'A');
            if ((seen & bit) != 0)
                duplicate = true;
            seen |= bit;
        }
        for (int value : count)
            if (value != 0)
                return false;
        if (duplicate)
            return true;
        int[] permutation = new int[FACES];
        for (int i = 0; i < FACES; i++)
            while (a[permutation[i]] != b[i])
                permutation[i]++;
        int inversions = 0;
        for (int i = 0; i < FACES; i++)
            for (int j = i + 1; j < FACES; j++)
                if (permutation[i] > permutation[j])
                    inversions++;
        return inversions % 2 == 0;
    }

    static char[] coloring() throws java.io.IOException {
        char[] result = new char[FACES];
        for (int i = 0; i < FACES; i++) {
            int ch = System.in.read();
            while (ch <= ' ')
                ch = System.in.read();
            result[i] = (char)ch;
        }
        return result;
    }

    public static void main(String[] args) throws Exception {
        char[] a = coloring(), b = coloring();
        System.out.println(equivalent(a, b) ? "equal" : "different");
    }
}
