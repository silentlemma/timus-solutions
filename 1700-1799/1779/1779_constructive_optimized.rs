use std::io::{self, BufWriter, Write};

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let n: usize = line.trim().parse().unwrap();
    let mut out = BufWriter::new(io::stdout().lock());
    // Grouping pairs by the larger endpoint gives floor(n/2) * ceil(n/2).
    let half = n / 2;
    writeln!(out, "{}", half * (n - half)).unwrap();
    for i in 1..=n {
        let first = (i + 1).max(n - i + 1);
        for j in first..=n {
            writeln!(out, "{} {}", i, j).unwrap();
        }
    }
    out.flush().unwrap();
}
