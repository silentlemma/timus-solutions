use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let duration: i32 = tokens.next().unwrap().parse().unwrap();
    let start: i32 = tokens.next().unwrap().parse().unwrap();
    let stdout = io::stdout();
    let mut output = io::BufWriter::new(stdout.lock());
    for _ in 0..count {
        let other: i32 = tokens.next().unwrap().parse().unwrap();
        let doubled_time = start + duration + other;
        let fraction = if doubled_time % 2 == 0 {
            "000000"
        } else {
            "500000"
        };
        writeln!(output, "{}.{}", doubled_time / 2, fraction).unwrap();
    }
}
