import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[] taken = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            taken[i] = (int)in.nval;
        }
        // the pocket is a stack: roll the balls in order, and whenever the top
        // one is the next ball the inspector took out, take it out
        int[] pocket = new int[n];
        int top = 0, next = 0;
        for (int ball = 1; ball <= n; ball++) {
            pocket[top++] = ball;
            while (top > 0 && next < n && pocket[top - 1] == taken[next]) {
                top--;
                next++;
            }
        }
        System.out.println(next == n ? "Not a proof" : "Cheater");
    }
}
