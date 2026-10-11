use std::io::{self, Read};

const DIGITS: usize = 19;
// a digit of any input sits at a power of ten from -SHIFT up to TOP - SHIFT
const SHIFT: i64 = 300;
const TOP: usize = 450;
const BASE: i64 = 10;
const HALF: i64 = 5;

// adds the decimal number in text, digit by digit, to the signed sums
fn add(text: &str, sum: &mut [i64]) {
    let (mantissa, exp) = match text.find(|c| c == 'e' || c == 'E') {
        Some(e) => (&text[..e], text[e + 1..].parse::<i64>().unwrap()),
        None => (text, 0),
    };
    let (sign, mantissa) = match mantissa.as_bytes()[0] {
        b'-' => (-1, &mantissa[1..]),
        b'+' => (1, &mantissa[1..]),
        _ => (1, mantissa),
    };
    let whole = mantissa.find('.').unwrap_or(mantissa.len()) as i64;
    let mut place = whole - 1 + exp;
    for c in mantissa.bytes().filter(|&c| c != b'.') {
        sum[(SHIFT + place) as usize] += sign * (c - b'0') as i64;
        place -= 1;
    }
}

// turns the sums into digits 0..9 and returns the carry out of the top
fn settle(sum: &mut [i64]) -> i64 {
    let mut carry = 0;
    for d in sum.iter_mut() {
        carry += *d;
        *d = carry.rem_euclid(BASE);
        carry = (carry - *d) / BASE;
    }
    carry
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut sum = vec![0i64; TOP];
    for w in words.take(n) {
        add(w, &mut sum);
    }
    let mut sign = "";
    if settle(&mut sum) < 0 {
        // a negative total: settle its opposite instead
        for d in sum.iter_mut() {
            *d = -*d;
        }
        sign = "-";
        settle(&mut sum);
    }
    let top = match sum.iter().rposition(|&d| d != 0) {
        Some(t) => t,
        None => {
            println!("0.{}e0", "0".repeat(DIGITS - 1));
            return;
        }
    };
    // keep 19 significant digits, rounding half up on the next one; kept[0]
    // takes a carry out of the first digit
    let mut kept = vec![0i64; DIGITS + 1];
    for k in 0..DIGITS {
        kept[k + 1] = if top >= k { sum[top - k] } else { 0 };
    }
    if top >= DIGITS && sum[top - DIGITS] >= HALF {
        let mut k = DIGITS;
        kept[k] += 1;
        while kept[k] == BASE {
            kept[k] = 0;
            k -= 1;
            kept[k] += 1;
        }
    }
    let (mut exponent, first) = (top as i64 - SHIFT, if kept[0] == 1 { 0 } else { 1 });
    if first == 0 {
        exponent += 1;
    }
    let text: String = kept[first..first + DIGITS]
        .iter()
        .map(|d| (b'0' + *d as u8) as char)
        .collect();
    println!("{}{}.{}e{}", sign, &text[..1], &text[1..], exponent);
}
