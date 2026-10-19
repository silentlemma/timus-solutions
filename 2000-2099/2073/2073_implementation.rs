use std::io::{self, Read};

const NAME_WIDTH: usize = 30;
const DATE_WIDTH: usize = 8;
const LETTERS: &str = "ABCDEFGHIJKLM";

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines().map(|l| l.trim());
    let border = format!(
        "+{}+{}+{}+\n",
        "-".repeat(NAME_WIDTH),
        "-".repeat(DATE_WIDTH),
        "-".repeat(LETTERS.len())
    );
    let mut out = border.clone();
    out += &format!(
        "|{:<w$}|{:<d$}|{}|\n",
        "Contest name",
        "Date",
        LETTERS,
        w = NAME_WIDTH,
        d = DATE_WIDTH
    );
    out += &border;
    let n: usize = lines.next().unwrap().parse().unwrap();
    for _ in 0..n {
        let name = lines.next().unwrap();
        let date = lines.next().unwrap();
        let counts: Vec<usize> =
            lines.next().unwrap().split_whitespace().map(|t| t.parse().unwrap()).collect();
        let (p, s) = (counts[0], counts[1]);
        // '.' for a given problem, 'x' once submitted, 'o' once accepted
        let mut marks = vec![b' '; LETTERS.len()];
        for m in marks.iter_mut().take(p) {
            *m = b'.';
        }
        for _ in 0..s {
            let submit = lines.next().unwrap();
            let i = (submit.as_bytes()[0] - b'A') as usize;
            if &submit[2..] == "Accepted" {
                marks[i] = b'o';
            } else if marks[i] != b'o' {
                marks[i] = b'x';
            }
        }
        out += &format!(
            "|{:<w$}|{}|{}|\n",
            name,
            date,
            String::from_utf8(marks).unwrap(),
            w = NAME_WIDTH
        );
        out += &border;
    }
    print!("{}", out);
}
