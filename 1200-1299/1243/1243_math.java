import java.io.*;

public class Main {
    static final int DWARFS = 7;

    public static void main(String[] args) throws IOException {
        String digits = new BufferedReader(new InputStreamReader(System.in)).readLine().trim();
        // the number has up to 51 digits, so take it modulo 7 digit by digit
        int rest = 0;
        for (char d : digits.toCharArray())
            rest = (rest * 10 + (d - '0')) % DWARFS;
        System.out.println(rest);
    }
}
