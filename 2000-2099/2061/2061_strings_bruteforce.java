import java.util.Scanner;

public class Main {
  // binary rich words of lengths 1..61 (OEIS A216264), counted offline by a search
  // over rich words with an eertree, 2061_strings_bruteforce_table.py
  private static final long[] RICH = {
    2L, 4L, 8L, 16L,
    32L, 64L, 128L, 252L,
    488L, 932L, 1756L, 3246L,
    5916L, 10618L, 18800L, 32846L,
    56704L, 96702L, 163184L, 272460L,
    450586L, 738274L, 1199376L, 1932338L,
    3089518L, 4903164L, 7728120L, 12099440L,
    18825066L, 29112876L, 44767202L, 68461866L,
    104153666L, 157657852L, 237510110L, 356158688L,
    531729840L, 790476048L, 1170354912L, 1725978316L,
    2535782098L, 3711932174L, 5414527812L, 7871216066L,
    11405072346L, 16472995026L, 23719943936L, 34053444354L,
    48748102876L, 69588917894L, 99071049592L, 140673083164L,
    199235958260L, 281479919278L, 396717767314L, 557825677390L,
    782576306282L, 1095448703190L, 1530103385844L, 2132734033216L,
    2966632985826L,
  };

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    StringBuilder out = new StringBuilder();
    for (int i = 0; i < n; ++i) out.append(RICH[i]).append('\n');
    System.out.print(out);
  }
}
