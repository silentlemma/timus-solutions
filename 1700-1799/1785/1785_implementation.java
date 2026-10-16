import java.util.Scanner;

public class Main {
    // the smallest number for each word, from the largest down
    static final int[] FROM = {1000, 500, 250, 100, 50, 20, 10, 5, 1};
    static final String[] WORDS = {
        "legion", "zounds", "swarm", "throng", "horde", "lots", "pack", "several", "few"
    };

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        int i = 0;
        while (n < FROM[i]) i++;
        System.out.println(WORDS[i]);
    }
}
