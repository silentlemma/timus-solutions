import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static class Input {
        final StreamTokenizer input =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int next() throws IOException {
            input.nextToken();
            return (int)input.nval;
        }
    }
    static int[] locate(int[] left, int[] right, int[] queries) {
        int[] stack = new int[left.length], answers = new int[queries.length];
        int size = 0, index = 0;
        for (int q = 0; q < queries.length; q++) {
            int point = queries[q];
            while (index < left.length && left[index] <= point) {
                while (size > 0 && right[stack[size - 1]] < left[index])
                    size--;
                stack[size++] = index++;
            }
            while (size > 0 && right[stack[size - 1]] < point)
                size--;
            answers[q] = size == 0 ? -1 : stack[size - 1] + 1;
        }
        return answers;
    }
    public static void main(String[] args) throws IOException {
        Input in = new Input();
        int n = in.next();
        int[] left = new int[n], right = new int[n];
        for (int i = 0; i < n; i++) {
            left[i] = in.next();
            right[i] = in.next();
        }
        int m = in.next();
        int[] queries = new int[m];
        for (int i = 0; i < m; i++)
            queries[i] = in.next();
        StringBuilder out = new StringBuilder();
        for (int answer : locate(left, right, queries))
            out.append(answer).append('\n');
        System.out.print(out);
    }
}
