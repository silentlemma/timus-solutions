import java.io.IOException;

public class Main {
    private static final int MAX_LENGTH = 200000;
    private static final int BUFFER_SIZE = 1024;

    public static void main(String[] args) throws IOException {
        // the letters go straight from 1 KB input blocks onto a fixed stack
        byte[] stack = new byte[MAX_LENGTH];
        byte[] buffer = new byte[BUFFER_SIZE];
        int size = 0;
        int length;
        while ((length = System.in.read(buffer)) != -1) {
            for (int i = 0; i < length; i++) {
                byte ch = buffer[i];
                if (ch < 'a' || ch > 'z')
                    continue;
                // a letter equal to the one before it cancels that one: removing the
                // inserted pairs in any order leaves the same text
                if (size > 0 && stack[size - 1] == ch)
                    size--;
                else
                    stack[size++] = ch;
            }
        }
        System.out.write(stack, 0, size);
        System.out.write('\n');
        System.out.flush();
    }
}
