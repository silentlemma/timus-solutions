public class Main {

    // refill a small buffer instead of retaining the input or allocating tokens.
    static final int BUFFER_SIZE = 4096;
    static final byte[] BUFFER = new byte[BUFFER_SIZE];
    static int position, length;
    static int read() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(BUFFER);
            position = 0;
            if (length < 0)
                return -1;
        }
        return Byte.toUnsignedInt(BUFFER[position++]);
    }

    static final String TRAM = "tram";
    static final String TROLLEY = "trolleybus";
    public static void main(String[] args) throws java.io.IOException {
        int wordLength = 0, trams = 0, trolleys = 0;
        boolean tram = true, trolley = true;
        for (int c = read();; c = read()) {
            // compare only the two target prefixes; no whole words or regex tokens are stored.
            if (c >= 'a' && c <= 'z') {
                tram = tram && wordLength < TRAM.length() && c == TRAM.charAt(wordLength);
                trolley =
                    trolley && wordLength < TROLLEY.length() && c == TROLLEY.charAt(wordLength);
                wordLength++;
            } else {
                if (tram && wordLength == TRAM.length())
                    trams++;
                if (trolley && wordLength == TROLLEY.length())
                    trolleys++;
                wordLength = 0;
                tram = trolley = true;
                if (c < 0)
                    break;
            }
        }
        System.out.println(trams > trolleys   ? "Tram driver"
                           : trolleys > trams ? "Trolleybus driver"
                                              : "Bus driver");
    }
}
