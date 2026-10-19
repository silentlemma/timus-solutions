public class Main {
  static final int HEIGHT = 6;
  static final int WIDTH = 11;

  public static void main(String[] args) {
    String[] grid = {
        ">?v........", ".>>.......v", "..@A+AB+B-<", "..B........", "..-........", ".^@A!#....."};
    System.out.println(HEIGHT + " " + WIDTH);
    for (String row : grid) System.out.println(row);
  }
}
