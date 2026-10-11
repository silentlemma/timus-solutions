use std::io::{self, Read};

const TOP: usize = 1_000_000; // 10000.00 in cents
const CENTS: i64 = 100;
const DIGITS: usize = 2;

// a price with at most two decimals, in cents
fn cents(s: &str) -> usize {
    let (whole, frac) = match s.find('.') {
        Some(dot) => (&s[..dot], &s[dot + 1..]),
        None => (s, ""),
    };
    let frac = format!("{}00", frac);
    let w: usize = if whole.is_empty() {
        0
    } else {
        whole.parse().unwrap()
    };
    w * CENTS as usize + frac[..DIGITS].parse::<usize>().unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    // bids counted by price, indexed from the highest price down, so that
    // "at least X" is a Fenwick prefix sum
    let mut tree = vec![0i64; TOP + 1];
    let mut sold: i64 = 0;
    while let Some(kind) = words.next() {
        if kind == "QUIT" {
            break;
        }
        let mut r = TOP + 1 - cents(words.next().unwrap());
        if kind == "SALE" {
            let k: i64 = words.next().unwrap().parse().unwrap();
            let mut count = 0;
            while r > 0 {
                count += tree[r];
                r &= r - 1;
            }
            sold += count.min(k);
        } else {
            let step = if kind == "BID" { 1 } else { -1 };
            while r <= TOP {
                tree[r] += step;
                r += r & r.wrapping_neg();
            }
        }
    }
    // the exchange earns one cent per piece sold
    println!("{}.{:02}", sold / CENTS, sold % CENTS);
}
