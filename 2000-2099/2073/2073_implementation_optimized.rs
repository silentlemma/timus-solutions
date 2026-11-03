use std::io::{self, BufRead, Write};

const NAME_WIDTH: usize = 30;
const DATE_WIDTH: usize = 8;
const LETTERS: &str = "ABCDEFGHIJKLM";

fn line<'a>(input: &mut impl BufRead, text: &'a mut String) -> &'a str {
    text.clear();
    input.read_line(text).unwrap();
    text.trim_end()
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    let mut text = String::new();
    let n: usize = line(&mut input, &mut text).trim().parse().unwrap();
    let border = format!(
        "+{}+{}+{}+\n",
        "-".repeat(NAME_WIDTH),
        "-".repeat(DATE_WIDTH),
        "-".repeat(LETTERS.len())
    );
    write!(
        out,
        "{}|{:<w$}|{:<d$}|{}|\n{}",
        border,
        "Contest name",
        "Date",
        LETTERS,
        border,
        w = NAME_WIDTH,
        d = DATE_WIDTH
    )
    .unwrap();
    for _ in 0..n {
        let name = line(&mut input, &mut text).to_owned();
        let date = line(&mut input, &mut text).to_owned();
        let mut counts = line(&mut input, &mut text).split_whitespace();
        let p: usize = counts.next().unwrap().parse().unwrap();
        let s: usize = counts.next().unwrap().parse().unwrap();
        let mut marks = [b' '; LETTERS.len()];
        marks[..p].fill(b'.');
        for _ in 0..s {
            let submit = line(&mut input, &mut text).as_bytes();
            let problem = usize::from(submit[0] - b'A');
            // Of the six allowed verdicts, only Accepted begins with A.
            if submit[2] == b'A' {
                marks[problem] = b'o';
            } else if marks[problem] != b'o' {
                marks[problem] = b'x';
            }
        }
        writeln!(
            out,
            "|{:<w$}|{}|{}|",
            name,
            date,
            String::from_utf8_lossy(&marks),
            w = NAME_WIDTH
        )
        .unwrap();
        out.write_all(border.as_bytes()).unwrap();
    }
}
