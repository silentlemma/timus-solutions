import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String text = in.readLine().trim();
        // a letter equal to the one before it cancels that one: removing the
        // inserted pairs in any order leaves the same text
        StringBuilder stack = new StringBuilder();
        for (char c : text.toCharArray()) {
            int n = stack.length();
            if (n > 0 && stack.charAt(n - 1) == c)
                stack.setLength(n - 1);
            else
                stack.append(c);
        }
        System.out.println(stack);
    }
}
