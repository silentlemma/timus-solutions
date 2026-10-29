public class Main {
    private static final int KIND_COUNT = 3;
    private static final int BUFFER_SIZE = 256;

    public static void main(String[] args) throws java.io.IOException {
        int[] counts = new int[KIND_COUNT];
        String[] names = {"Emperor Penguin", "Little Penguin", "Macaroni Penguin"};
        byte[] buffer = new byte[BUFFER_SIZE];
        // every record is two words, the kind and "Penguin"
        // the kinds start with the capitals E, L and M, and "Penguin" has none of
        // them, so counting those letters in 256-byte blocks counts the kinds
        int length;
        while ((length = System.in.read(buffer)) > 0) {
            for (int i = 0; i < length; i++) {
                switch (buffer[i]) {
                case 'E':
                    counts[0]++;
                    break;
                case 'L':
                    counts[1]++;
                    break;
                case 'M':
                    counts[2]++;
                    break;
                default:
                    break;
                }
            }
        }
        int best = 0;
        for (int i = 1; i < KIND_COUNT; i++)
            if (counts[i] > counts[best])
                best = i;
        System.out.println(names[best]);
    }
}
