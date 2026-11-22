public class Main {

    static final int SIDE = 4, CELLS = SIDE * SIDE, INPUT_SIZE = 64;
    static final byte[] input = new byte[INPUT_SIZE];
    static int position, available;
    static int nextCharacter() throws java.io.IOException {
        int c;
        do {
            if (position == available) {
                available = System.in.read(input);
                position = 0;
                if (available < 0)
                    return -1;
            }
            c = input[position++];
        } while (c <= ' ');
        return c;
    }
    static int rotate(int mask) {
        int turned = 0;
        while (mask != 0) {
            int cell = Integer.numberOfTrailingZeros(mask);
            mask &= mask - 1;
            turned |= 1 << (SIDE * (cell % SIDE) + SIDE - 1 - cell / SIDE);
        }
        return turned;
    }

    static byte[] decode(int mask, byte[] sheet) {
        byte[] answer = new byte[CELLS + 1];
        int length = 0;
        for (int turn = 0; turn < SIDE; turn++) {
            for (int holes = mask; holes != 0; holes &= holes - 1)
                answer[length++] = sheet[Integer.numberOfTrailingZeros(holes)];
            mask = rotate(mask);
        }
        answer[length] = '\n';
        return answer;
    }

    public static void main(String[] args) throws java.io.IOException {
        int mask = 0;
        for (int cell = 0; cell < CELLS; cell++)
            if (nextCharacter() == 'X')
                mask |= 1 << cell;
        byte[] sheet = new byte[CELLS];
        for (int cell = 0; cell < CELLS; cell++)
            sheet[cell] = (byte)nextCharacter();
        System.out.write(decode(mask, sheet));
    }
}
