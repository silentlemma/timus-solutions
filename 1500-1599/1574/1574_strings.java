import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        String line = new BufferedReader(new InputStreamReader(System.in)).readLine().trim();
        // the balance after each prefix; a shift that starts right after a prefix
        // of the lowest balance never goes below zero, any other shift does
        int balance = 0, lowest = 0, count = 0;
        for (int i = 0; i < line.length(); i++) {
            balance += line.charAt(i) == '(' ? 1 : -1;
            if (i == 0 || balance < lowest) {
                lowest = balance;
                count = 1;
            } else if (balance == lowest)
                count++;
        }
        System.out.println(balance == 0 ? count : 0);
    }
}
