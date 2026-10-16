use std::collections::HashMap;
use std::io::{self, Read};

const R_NUM: i64 = 8314;
const R_DEN: i64 = 1000;
const SCALE: i64 = 1000000;
const LINE: usize = 3; // tokens in "X = value"

fn print_value(name: &str, numerator: i64, denominator: i64) {
    let value = (numerator * SCALE + denominator / 2) / denominator;
    println!("{} = {}.{:06}", name, value / SCALE, value % SCALE);
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    // lines "X = value"
    let tokens: Vec<&str> = input.split_ascii_whitespace().collect();
    let known: HashMap<&str, i64> =
        tokens.chunks(LINE).map(|c| (c[0], c[2].parse::<i64>().unwrap())).collect();
    let get = |name: &str| known.get(name).copied();
    let (p, n, v, t) = (get("p"), get("n"), get("V"), get("T"));
    // p V = n R T, with V and T strictly positive
    match (p, n, v, t) {
        (None, Some(n), Some(v), Some(t)) => print_value("p", n * R_NUM * t, R_DEN * v),
        (Some(p), None, Some(v), Some(t)) => print_value("n", p * v * R_DEN, R_NUM * t),
        (Some(p), Some(n), _, _) => {
            // the unknown is V (beside p) or T (beside n R), and both must
            // be positive: a zero factor leaves 0 = 0 or a contradiction
            let find_v = v.is_none();
            let (factor, other) = if find_v { (p, n) } else { (n, p) };
            if factor == 0 && other == 0 {
                println!("undefined");
            } else if factor == 0 || other == 0 {
                println!("error");
            } else if find_v {
                print_value("V", n * R_NUM * t.unwrap(), R_DEN * p);
            } else {
                print_value("T", p * v.unwrap() * R_DEN, n * R_NUM);
            }
        }
        _ => {}
    }
}
