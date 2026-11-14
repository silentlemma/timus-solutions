import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;
import java.util.Locale;

public class Main {
    private static final double MIN_ROPE = 1.0;
    private static final double MAX_ROPE = 50.0;
    private static final double MIN_SEPARATION = 2 * MIN_ROPE;
    private static final double EPS = 1e-9;

    private static class Tree {
        final double x, y;
        double capSquared = MAX_ROPE * MAX_ROPE;
        double cap;

        Tree(double x, double y) {
            this.x = x;
            this.y = y;
        }

        double separationSquared(Tree other) {
            double dx = x - other.x, dy = y - other.y;
            return dx * dx + dy * dy;
        }
    }

    private static double maximum(Tree[] trees) {
        for (int i = 0; i < trees.length; ++i) {
            Tree a = trees[i];
            for (int j = i + 1; j < trees.length; ++j) {
                Tree b = trees[j];
                double squared = a.separationSquared(b);
                a.capSquared = Math.min(a.capSquared, squared);
                b.capSquared = Math.min(b.capSquared, squared);
            }
            a.cap = Math.sqrt(a.capSquared);
        }
        Arrays.sort(trees, (a, b) -> Double.compare(b.capSquared, a.capSquared));
        double best = 0;
        for (int i = 0; i + 1 < trees.length; ++i) {
            Tree a = trees[i];
            if (a.capSquared + trees[i + 1].capSquared <= best) {
                break;
            }
            for (int j = i + 1; j < trees.length; ++j) {
                Tree b = trees[j];
                double upper = a.capSquared + b.capSquared;
                if (upper <= best || b.cap < MIN_ROPE - EPS) {
                    break;
                }
                double squared = a.separationSquared(b);
                double sum = a.cap + b.cap;
                if (squared >= sum * sum) {
                    best = upper;
                    break;
                }
                if (squared < MIN_SEPARATION * MIN_SEPARATION - EPS) {
                    continue;
                }
                // A binding distance constraint needs only the two endpoints.
                double distance = Math.sqrt(squared);
                double longA = Math.min(a.cap, distance - MIN_ROPE);
                double longB = Math.min(b.cap, distance - MIN_ROPE);
                double shortA = distance - longB, shortB = distance - longA;
                best = Math.max(best, Math.max(longA * longA + shortB * shortB,
                                               shortA * shortA + longB * longB));
            }
        }
        return best * Math.PI;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer input =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        input.nextToken();
        Tree[] trees = new Tree[(int)input.nval];
        for (int i = 0; i < trees.length; ++i) {
            input.nextToken();
            double x = input.nval;
            input.nextToken();
            trees[i] = new Tree(x, input.nval);
        }
        System.out.printf(Locale.US, "%.4f%n", maximum(trees));
    }
}
