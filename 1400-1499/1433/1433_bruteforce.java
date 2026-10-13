import java.util.Scanner;

public class Main {
    static final int FACES = 4;
    static String a, b;
    static boolean same = false;

    static void tryAll(int[] p, int size, int used) {
        if (size == FACES) {
            int inversions = 0;
            for (int i = 0; i < FACES; i++)
                for (int j = i + 1; j < FACES; j++)
                    if (p[i] > p[j])
                        inversions++;
            // the rotations of a tetrahedron move its faces by exactly the even permutations
            if (inversions % 2 != 0)
                return;
            for (int i = 0; i < FACES; i++)
                if (b.charAt(i) != a.charAt(p[i]))
                    return;
            same = true;
            return;
        }
        for (int k = 0; k < FACES; k++)
            if ((used >> k & 1) == 0) {
                p[size] = k;
                tryAll(p, size + 1, used | 1 << k);
            }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        a = in.next();
        b = in.next();
        tryAll(new int[FACES], 0, 0);
        System.out.println(same ? "equal" : "different");
    }
}
