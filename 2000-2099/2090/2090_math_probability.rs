use std::io::{self, Read};

const DECIMAL_PLACES: usize = 12;

fn probability(numerator: i64, denominator: i64) -> String {
    let mut fraction = 0;
    let mut remainder = numerator;
    let mut scale = 1;
    for _ in 0..DECIMAL_PLACES {
        remainder *= 10;
        fraction = fraction * 10 + remainder / denominator;
        remainder %= denominator;
        scale *= 10;
    }
    if 2 * remainder >= denominator {
        fraction += 1;
    }
    let integer = (fraction / scale).to_string();
    fraction %= scale;
    if fraction == 0 {
        return integer;
    }
    let digits = format!("{:0width$}", fraction, width = DECIMAL_PLACES);
    format!("{}.{}", integer, digits.trim_end_matches('0'))
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input
        .split_whitespace()
        .map(|token| token.parse::<i64>().unwrap());
    let speed = values.next().unwrap();
    let _ = values.next();
    let _ = values.next();
    let width_marx = values.next().unwrap();
    let green_engels = values.next().unwrap();
    let yellow_engels = values.next().unwrap();
    let green_marx = values.next().unwrap();
    let yellow_marx = values.next().unwrap();
    let period = green_engels + yellow_engels + green_marx + yellow_marx;
    let denominator = speed * period;
    // Only the phase lengths and the time to cross Marx affect the comparison.
    let crosswalk = speed * (green_engels + yellow_marx) - width_marx;
    println!(
        "{} {}",
        probability(crosswalk, denominator),
        probability(width_marx, denominator)
    );
}
