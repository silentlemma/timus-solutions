use std::io::{self, Read};

const TOTAL: usize = 1000;
const MAX_ODD: usize = 100;
const OUTCOMES: usize = 3;
const BASE: u64 = 1000000000;
const DIGITS: usize = 9;
type Big = Vec<u64>;

fn trim(a: &mut Big) {
    while a.len() > 1 && a.last() == Some(&0) {
        a.pop();
    }
}

fn number(text: &str) -> Big {
    let text = text.trim_start_matches('+');
    let mut a = Vec::new();
    let mut end = text.len();
    while end > 0 {
        let start = end.saturating_sub(DIGITS);
        a.push(text[start..end].parse().unwrap());
        end = start;
    }
    trim(&mut a);
    a
}

fn multiply(a: &Big, b: &Big) -> Big {
    let mut c = vec![0; a.len() + b.len()];
    for i in 0..a.len() {
        let mut carry = 0;
        let mut j = 0;
        while j < b.len() || carry > 0 {
            let mut value = c[i + j] + carry;
            if j < b.len() {
                value += a[i] * b[j];
            }
            c[i + j] = value % BASE;
            carry = value / BASE;
            j += 1;
        }
    }
    trim(&mut c);
    c
}

fn add(a: &Big, b: &Big) -> Big {
    let mut c = Vec::new();
    let mut carry = 0;
    let mut i = 0;
    while i < a.len().max(b.len()) || carry > 0 {
        let mut value = carry;
        if i < a.len() { value += a[i]; }
        if i < b.len() { value += b[i]; }
        c.push(value % BASE);
        carry = value / BASE;
        i += 1;
    }
    c
}

fn shift(a: &Big, scale: usize) -> Big {
    let factor = 10_u64.pow((scale % DIGITS) as u32);
    let mut c = vec![0; scale / DIGITS];
    c.extend(multiply(a, &number(&factor.to_string())));
    c
}

fn at_least(a: &Big, b: &Big) -> bool {
    if a.len() != b.len() {
        return a.len() > b.len();
    }
    a.iter().rev().cmp(b.iter().rev()) != std::cmp::Ordering::Less
}

fn decimal(token: &str) -> (Big, usize) {
    let lower = token.to_ascii_lowercase();
    let parts: Vec<&str> = lower.split('e').collect();
    let mantissa = parts[0];
    let exponent: i64 = if parts.len() == 2 { parts[1].parse().unwrap() } else { 0 };
    let mut scale = match mantissa.find('.') {
        Some(point) => (mantissa.len() - point - 1) as i64,
        None => 0,
    } - exponent;
    let mut value = number(&mantissa.replace('.', ""));
    if scale < 0 {
        value = shift(&value, (-scale) as usize);
        scale = 0;
    }
    (value, scale as usize)
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut numerator = number("1");
    let mut denominator = number("0");
    for token in text.split_ascii_whitespace() {
        let (value, scale) = decimal(token);
        denominator = add(&multiply(&denominator, &value), &shift(&numerator, scale));
        numerator = multiply(&numerator, &value);
    }
    numerator = multiply(&numerator, &number(&TOTAL.to_string()));
    // betting in proportion to 1 / k on every outcome pays the same whatever
    // happens, and any other split pays less on some outcome
    let mut low = 0;
    let mut high = TOTAL * MAX_ODD / OUTCOMES + 1;
    while low + 1 < high {
        let middle = (low + high) / 2;
        if at_least(&multiply(&numerator, &number("2")),
                    &multiply(&denominator, &number(&(2 * middle - 1).to_string()))) {
            low = middle;
        } else {
            high = middle;
        }
    }
    println!("{}", low);
}
