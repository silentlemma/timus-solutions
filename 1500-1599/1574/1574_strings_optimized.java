public class Main {
    static final int BUFFER_SIZE = 16384;

    public static void main(String[] args) throws java.io.IOException {
        byte[] block = new byte[BUFFER_SIZE];
        int balance = 0, lowest = 0, count = 0;
        for (int size; (size = System.in.read(block)) >= 0;) {
            for (int i = 0; i < size; i++) {
                byte character = block[i];
                if (character != '(' && character != ')')
                    continue;
                balance += character == '(' ? 1 : -1;
                if (balance < lowest) {
                    lowest = balance;
                    count = 1;
                } else if (balance == lowest)
                    count++;
            }
        }
        System.out.println(balance == 0 ? count : 0);
    }
}
