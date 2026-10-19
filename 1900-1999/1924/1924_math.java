import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int size = input.nextInt();
        int total = size * (size + 1) / 2;
        System.out.println(total % 2 == 0 ? "black" : "grimy");
    }
}
