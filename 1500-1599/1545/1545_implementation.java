import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String[] words = new String[n];
        for (int i = 0; i < n; i++)
            words[i] = in.next();
        char letter = in.next().charAt(0);
        // the dictionary order is kept, repeated entries are printed every time
        StringBuilder out = new StringBuilder();
        for (String w : words)
            if (w.charAt(0) == letter)
                out.append(w).append('\n');
        System.out.print(out);
    }
}
