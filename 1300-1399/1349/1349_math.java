import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // by Fermat's last theorem only the first and second powers have answers
        if (n == 1)
            System.out.println("1 2 3");
        else if (n == 2)
            System.out.println("3 4 5");
        else
            System.out.println(-1);
    }
}
