use std::io::{self, Read};

const BASE: i32 = 10;

// the chance that two random digits from first .. 9 plus the incoming
// carry reach 10
fn carry_chance(first: i32, extra: i32) -> f64 {
    let side = BASE - first;
    let hits = (first..BASE)
        .flat_map(|a| (first..BASE).map(move |b| a + b + extra))
        .filter(|&s| s >= BASE)
        .count();
    hits as f64 / (side * side) as f64
}

// the chance that one place with digits from first .. 9 shows a and b
fn pair_chance(first: i32, a: i32, b: i32) -> f64 {
    let side = (BASE - first) as f64;
    (if a == b { 1.0 } else { 2.0 }) / (side * side)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let k: i32 = match input.trim().parse() {
        Ok(v) => v,
        Err(_) => return,
    };
    // every place costs one written digit and one sum; a carry costs a mark
    // and, unless it leaves the last place, one more second to add it in,
    // a carry out of the last place is written as a digit
    let mut expected = 2.0 * k as f64;
    let mut carry = 0.0;
    for place in 0..k {
        let first = if place == k - 1 { 1 } else { 0 };
        carry = (1.0 - carry) * carry_chance(first, 0) + carry * carry_chance(first, 1);
        expected += 2.0 * carry;
    }
    // the first sum of two digits both above 1 takes a second more
    for a in 2..BASE {
        for b in a..BASE {
            let miss = (1.0 - pair_chance(0, a, b)).powi(k - 1) * (1.0 - pair_chance(1, a, b));
            expected += 1.0 - miss;
        }
    }
    println!("{:.8}", expected);
}
