import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static final int WIDTH = 80;

    public static void main(String[] args) throws IOException {
        String line = new BufferedReader(new InputStreamReader(System.in)).readLine();
        char[] screen = new char[WIDTH];
        Arrays.fill(screen, ' ');
        int cursor = 0;
        for (char key : (line == null ? "" : line).toCharArray()) {
            if (key == '<') {
                cursor--;
            } else if (key == '>') {
                cursor++;
            } else {
                screen[cursor++] = key;
            }
            // past either edge the cursor jumps to the leftmost position
            if (cursor < 0 || cursor >= WIDTH) {
                cursor = 0;
            }
        }
        System.out.println(new String(screen));
    }
}
