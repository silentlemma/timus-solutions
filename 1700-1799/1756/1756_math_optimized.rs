use std::io::{self, BufWriter, Read, Write};
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input
        .split_ascii_whitespace()
        .map(|w| w.parse::<u64>().unwrap());
    let (m, first_days, days) = (
        words.next().unwrap(),
        words.next().unwrap(),
        words.next().unwrap(),
    );
    // the work is m * first_days digger-days; spreading it as evenly as possible
    // over the given days needs the fewest diggers, the rounded-up average
    let (low, extra) = (m * first_days / days, m * first_days % days);
    // format the two counts once and stream them, avoiding up to 10000 allocated strings.
    let low_text = low.to_string();
    let high_text = (low + 1).to_string();
    let mut out = BufWriter::new(io::stdout().lock());
    for day in 0..days {
        if day > 0 {
            out.write_all(b" ").unwrap();
        }
        out.write_all(if day < days - extra {
            low_text.as_bytes()
        } else {
            high_text.as_bytes()
        })
        .unwrap();
    }
    writeln!(out).unwrap();
}
