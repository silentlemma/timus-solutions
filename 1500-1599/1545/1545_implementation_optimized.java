public class Main {
    private static final int WORD_LENGTH = 2;
    private static final int OUTPUT_LINE_LENGTH = WORD_LENGTH + 1;

    private static final int BUFFER_SIZE = 256;
    private static final byte[] buffer = new byte[BUFFER_SIZE];
    private static int position, length;

    // every hieroglyph is two letters, so the words and the answer are byte
    // arrays filled from 256-byte blocks, with no Scanner and no strings
    private static int readByte() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length < 0) {
                return -1;
            }
        }
        return buffer[position++];
    }

    private static int nextInt() throws java.io.IOException {
        int ch;
        do {
            ch = readByte();
        } while (ch >= 0 && ch <= ' ');
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = readByte();
        }
        return value;
    }

    private static byte nextLetter() throws java.io.IOException {
        int ch;
        do {
            ch = readByte();
        } while (ch >= 0 && ch <= ' ');
        return (byte)ch;
    }

    public static void main(String[] args) throws java.io.IOException {
        int count = nextInt();
        byte[] words = new byte[count * WORD_LENGTH];
        for (int i = 0; i < words.length; ++i) {
            words[i] = nextLetter();
        }
        byte letter = nextLetter();
        byte[] output = new byte[count * OUTPUT_LINE_LENGTH];
        int length = 0;
        // the dictionary order is kept, repeated entries are printed every time
        for (int i = 0; i < words.length; i += WORD_LENGTH) {
            if (words[i] == letter) {
                output[length++] = words[i];
                output[length++] = words[i + 1];
                output[length++] = '\n';
            }
        }
        System.out.write(output, 0, length);
        System.out.flush();
    }
}
