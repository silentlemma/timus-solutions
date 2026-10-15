import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int pages = in.nextInt(), cover = in.nextInt(), start = in.nextInt(), stop = in.nextInt();
        // on a shelf a volume's first page faces its right neighbour and its
        // last page faces the left one
        int whole = pages + 2 * cover, length;
        if (start == stop)
            length = pages;
        else if (start < stop)
            length = 2 * cover + (stop - start - 1) * whole;
        else
            length = 2 * pages + 2 * cover + (start - stop - 1) * whole;
        System.out.println(length);
    }
}
