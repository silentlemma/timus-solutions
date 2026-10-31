use std::io::{self, BufWriter, Read, Write};

const NOTES: &[i64] = &[10, 50, 100, 500, 1000, 5000];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut numbers = input.split_whitespace().map(|s| s.parse::<i64>().unwrap());
    let (mut total, mut smallest) = (0, 0);
    for &note in NOTES {
        let count = numbers.next().unwrap();
        total += count * note;
        if count > 0 && smallest == 0 {
            smallest = note;
        }
    }
    let price = numbers.next().unwrap();
    // k tickets fit when k * price <= total, and taking away the smallest
    // note must leave too little: total - smallest < k * price
    let low = (total - smallest) / price + 1;
    let high = total / price;
    // stream up to 5000 answers through one buffer instead of allocating their strings.
    let stdout = io::stdout();
    let mut out = BufWriter::new(stdout.lock());
    writeln!(out, "{}", high - low + 1).unwrap();
    for k in low..=high {
        write!(out, "{}{}", k, if k == high { "\n" } else { " " }).unwrap();
    }
}
