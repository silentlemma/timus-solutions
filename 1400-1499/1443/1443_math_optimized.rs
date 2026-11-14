use std::io::{self, Read};

const TICKS_PER_METER: f64 = 10_000.0;

fn ticks(token: &str) -> u32 {
    // Four decimal places leave plenty of margin before the nearest integer changes.
    (token.parse::<f64>().unwrap() * TICKS_PER_METER).round() as u32
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut fields = input.split_ascii_whitespace();
    let lines: u32 = fields.next().unwrap().parse().unwrap();
    let length = ticks(fields.next().unwrap());
    let rail = ticks(fields.next().unwrap());
    let mut total = lines * (length / rail);
    let remainder = length % rail;
    if remainder != 0 {
        total += lines.div_ceil(rail / remainder);
    }
    println!("{}", total);
    Ok(())
}
