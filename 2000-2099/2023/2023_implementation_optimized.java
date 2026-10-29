public class Main {
    private static final int BUFFER_SIZE = 256;

    public static void main(String[] args) throws java.io.IOException {
        byte[] buffer = new byte[BUFFER_SIZE];
        int position = 0;
        int steps = 0;
        int length;
        // the input is read in 256-byte blocks and scanned byte by byte; a label's
        // only capital letter is its first one, and the first letters
        // tell the positions apart: A P O R, B M S and the rest
        while ((length = System.in.read(buffer)) > 0) {
            for (int i = 0; i < length; i++) {
                int c = buffer[i];
                if (c < 'A' || c > 'Z')
                    continue;
                int target = 2;
                switch (c) {
                case 'A':
                case 'P':
                case 'O':
                case 'R':
                    target = 0;
                    break;
                case 'B':
                case 'M':
                case 'S':
                    target = 1;
                    break;
                default:
                    break;
                }
                steps += Math.abs(target - position);
                position = target;
            }
        }
        System.out.println(steps);
    }
}
