import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int harry = in.nextInt(), larry = in.nextInt();
        // the last can was shot by both, so each missed the other's count minus one
        System.out.println((larry - 1) + " " + (harry - 1));
    }
}
