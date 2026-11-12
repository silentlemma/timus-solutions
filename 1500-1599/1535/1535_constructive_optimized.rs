use std::io::{self, Read, Write};

const OUTPUT_SIZE: usize = 8192;
const PAIR_PERIOD: usize = 4;

fn number(output: &mut impl Write, first: &mut bool, value: usize) {
    if !*first {
        output.write_all(b" ").unwrap();
    }
    *first = false;
    write!(output, "{}", value).unwrap();
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let stdout = io::stdout();
    let mut output = io::BufWriter::with_capacity(OUTPUT_SIZE, stdout.lock());
    let mut first = true;
    number(&mut output, &mut first, 1);
    number(&mut output, &mut first, n);
    let pairs = (n - 1) / 2;
    // Direct arm indexing reproduces the original cycle without retaining any permutation.
    for k in 1..=pairs {
        number(
            &mut output,
            &mut first,
            if k % 2 == 1 { k + 1 } else { n - k },
        );
    }
    if n % 2 == 0 && n > 2 {
        number(&mut output, &mut first, 2 * (n / PAIR_PERIOD) + 1);
    }
    for k in (2..=pairs).rev() {
        number(
            &mut output,
            &mut first,
            if k % 2 == 1 { k } else { n - k + 1 },
        );
    }
    output.write_all(b"\n").unwrap();
    first = true;
    for value in (1..=n).step_by(2) {
        number(&mut output, &mut first, value);
    }
    for value in (2..=n - n % 2).rev().step_by(2) {
        number(&mut output, &mut first, value);
    }
    output.write_all(b"\n").unwrap();
    output.flush().unwrap();
}
