import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    // a binary search tree in arrays: the number of node v and its children,
    // -1 for a missing child
    static int[] number, leftChild, rightChild;
    static int size = 0;
    static StringBuilder out = new StringBuilder();

    static void insert(int value) {
        int node = size++;
        number[node] = value;
        leftChild[node] = rightChild[node] = -1;
        for (int v = 0; node > 0;) {
            int[] side = value < number[v] ? leftChild : rightChild;
            if (side[v] < 0) {
                side[v] = node;
                return;
            }
            v = side[v];
        }
    }

    // the even-session order: right wing, left wing, then the chairman
    static void speak(int v) {
        if (v < 0) {
            return;
        }
        speak(rightChild[v]);
        speak(leftChild[v]);
        out.append(number[v]).append('\n');
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[] post = new int[n];
        for (int k = 0; k < n; k++) {
            in.nextToken();
            post[k] = (int)in.nval;
        }
        number = new int[n];
        leftChild = new int[n];
        rightChild = new int[n];
        // read backwards, the odd-session order names every chairman before the
        // members of the wings, so inserting in that order rebuilds the tree
        for (int k = n - 1; k >= 0; k--) {
            insert(post[k]);
        }
        if (n > 0) {
            speak(0);
        }
        System.out.print(out);
    }
}
