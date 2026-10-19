import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static int minimumClicks(String[] words) {
        int capacity = 1;
        for (String word : words) {
            capacity += word.length();
        }
        int[] first = new int[capacity];
        int[] next = new int[capacity];
        char[] labels = new char[capacity];
        int size = 1;
        for (String word : words) {
            int node = 0;
            for (int index = 0; index < word.length(); index++) {
                char letter = word.charAt(index);
                int child = first[node];
                while (child != 0 && labels[child] != letter) {
                    child = next[child];
                }
                if (child == 0) {
                    child = size++;
                    next[child] = first[node];
                    labels[child] = letter;
                    first[node] = child;
                }
                node = child;
            }
        }
        int[] leaves = new int[size];
        int[] normal = new int[size];
        int[] supplied = new int[size];
        for (int node = size - 1; node >= 0; node--) {
            int child = first[node];
            if (child == 0) {
                leaves[node] = 1;
                continue;
            }
            int total = 0;
            int bestNormal = 0;
            int bestSupplied = 0;
            while (child != 0) {
                int count = leaves[child];
                leaves[node] += count;
                total += normal[child] + count;
                int saving = normal[child] - supplied[child];
                bestNormal = Math.max(bestNormal, saving);
                bestSupplied = Math.max(bestSupplied, count + saving);
                child = next[child];
            }
            normal[node] = total - bestNormal;
            supplied[node] = total - bestSupplied;
        }
        return normal[0];
    }

    private static String nextWord(BufferedInputStream in) throws IOException {
        StringBuilder word = new StringBuilder();
        int character = in.read();
        while (character <= ' ' && character != -1) {
            character = in.read();
        }
        while (character > ' ') {
            word.append((char) character);
            character = in.read();
        }
        return word.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream in = new BufferedInputStream(System.in);
        int count = Integer.parseInt(nextWord(in));
        String[] words = new String[count];
        for (int index = 0; index < count; index++) {
            words[index] = nextWord(in);
        }
        System.out.println(minimumClicks(words));
    }
}
