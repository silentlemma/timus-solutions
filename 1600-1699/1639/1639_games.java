import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m = in.nextInt(), n = in.nextInt();
        // every break adds one piece, so the game always lasts m * n - 1 moves
        System.out.println((m * n - 1) % 2 == 1 ? "[:=[first]" : "[second]=:]");
    }
}
