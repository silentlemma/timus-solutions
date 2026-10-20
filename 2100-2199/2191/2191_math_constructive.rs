use std::io::{self, Read, Write};

const DIGITS: usize = 18;

/// Appends a nonnegative fraction with at most DIGITS decimals, truncated.
fn number(out: &mut String, numerator: i64, denominator: i64) {
    out.push_str(&(numerator / denominator).to_string());
    let mut rest = numerator % denominator;
    if rest == 0 {
        return;
    }
    out.push('.');
    for _ in 0..DIGITS {
        rest *= 10;
        out.push((b'0' + (rest / denominator) as u8) as char);
        rest %= denominator;
    }
    while out.ends_with('0') {
        out.pop();
    }
    if out.ends_with('.') {
        out.pop();
    }
}

/// Writes c |x - root| with c = numerator / denominator as one term.
fn term(out: &mut String, mut numerator: i64, denominator: i64, root: i64, constant: bool) {
    if numerator < 0 {
        out.push('-');
        numerator = -numerator;
    } else if !out.is_empty() {
        out.push('+');
    }
    out.push('|');
    if constant {
        out.push_str("0x+");
        number(out, numerator, denominator);
    } else {
        let shift = numerator * root;
        number(out, numerator, denominator);
        out.push_str(if shift >= 0 { "x-" } else { "x+" });
        number(out, shift.abs(), denominator);
    }
    out.push('|');
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut xs = vec![0i64; n];
    let mut ys = vec![0i64; n];
    for i in 0..n {
        xs[i] = it.next().unwrap();
        ys[i] = it.next().unwrap();
    }
    let mut out = String::new();

    // A kink at x_i where the slope turns from s to t is (t - s) / 2 |x - x_i|.
    for i in 1..n - 1 {
        let (left_dx, left_dy) = (xs[i] - xs[i - 1], ys[i] - ys[i - 1]);
        let (right_dx, right_dy) = (xs[i + 1] - xs[i], ys[i + 1] - ys[i]);
        let turn = right_dy * left_dx - left_dy * right_dx;
        term(&mut out, turn, 2 * left_dx * right_dx, xs[i], false);
    }

    let (first_dx, first_dy) = (xs[1] - xs[0], ys[1] - ys[0]);
    let (last_dx, last_dy) = (xs[n - 1] - xs[n - 2], ys[n - 1] - ys[n - 2]);
    // On [x_1, x_N] the kinks add (t - s) / 2 times x - x_i; the term at x_1
    // restores the first slope and a constant fixes the value at x_1.
    term(&mut out, first_dy * last_dx + last_dy * first_dx, 2 * first_dx * last_dx, xs[0], false);
    let span = xs[n - 2] - xs[0];
    let constant = 2 * ys[0] * last_dx - last_dy * span + (ys[n - 2] - ys[0]) * last_dx;
    term(&mut out, constant, 2 * last_dx, 0, true);
    out.push('\n');
    io::stdout().write_all(out.as_bytes()).unwrap();
}
