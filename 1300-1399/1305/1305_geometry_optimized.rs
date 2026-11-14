use std::io::{self, Read, Write};

const DECIMAL: i32 = 10;

fn number(input: &mut impl Iterator<Item = io::Result<u8>>) -> i32 {
    let digits = input
        .by_ref()
        .map(Result::unwrap)
        .skip_while(u8::is_ascii_whitespace);
    digits
        .take_while(u8::is_ascii_digit)
        .fold(0, |value, ch| DECIMAL * value + i32::from(ch - b'0'))
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut input = io::BufReader::new(stdin.lock()).bytes();
    let count = number(&mut input);
    let (x, y) = (number(&mut input), number(&mut input));
    let (mut min_x, mut max_x) = (x, x);
    let (mut min_y, mut max_y) = (y, y);
    let (mut min_sum, mut max_sum) = (x + y, x + y);
    let (mut min_diff, mut max_diff) = (x - y, x - y);
    for _ in 1..count {
        let (x, y) = (number(&mut input), number(&mut input));
        min_x = min_x.min(x);
        max_x = max_x.max(x);
        min_y = min_y.min(y);
        max_y = max_y.max(y);
        min_sum = min_sum.min(x + y);
        max_sum = max_sum.max(x + y);
        min_diff = min_diff.min(x - y);
        max_diff = max_diff.max(x - y);
    }
    let corners = [
        (min_sum - min_y, min_y),
        (max_diff + min_y, min_y),
        (max_x, max_x - max_diff),
        (max_x, max_sum - max_x),
        (max_sum - max_y, max_y),
        (min_diff + max_y, max_y),
        (min_x, min_x - min_diff),
        (min_x, min_sum - min_x),
    ];
    let mut output = io::stdout().lock();
    let mut previous = corners[corners.len() - 1];
    let mut printed = false;
    for &(x, y) in &corners {
        if previous != (x, y) {
            writeln!(output, "{} {}", x, y)?;
            printed = true;
        }
        previous = (x, y);
    }
    if !printed {
        writeln!(output, "{} {}", previous.0, previous.1)?;
    }
    Ok(())
}
