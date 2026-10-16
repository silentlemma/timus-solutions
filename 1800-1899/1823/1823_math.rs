use std::collections::HashMap;
use std::io::{self, Read};

const R: f64 = 8.314;
const LINE: usize = 3; // tokens in "X = value"

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    // lines "X = value"
    let tokens: Vec<&str> = input.split_ascii_whitespace().collect();
    let known: HashMap<&str, f64> =
        tokens.chunks(LINE).map(|c| (c[0], c[2].parse::<f64>().unwrap())).collect();
    let get = |name: &str| known.get(name).copied();
    let (p, n, v, t) = (get("p"), get("n"), get("V"), get("T"));
    // p V = n R T, with V and T strictly positive
    match (p, n, v, t) {
        (None, Some(n), Some(v), Some(t)) => println!("p = {:.6}", n * R * t / v),
        (Some(p), None, Some(v), Some(t)) => println!("n = {:.6}", p * v / (R * t)),
        (Some(p), Some(n), _, _) => {
            // the unknown is V (beside p) or T (beside n R), and both must
            // be positive: a zero factor leaves 0 = 0 or a contradiction
            let find_v = v.is_none();
            let (factor, other) = if find_v { (p, n) } else { (n, p) };
            if factor == 0.0 && other == 0.0 {
                println!("undefined");
            } else if factor == 0.0 || other == 0.0 {
                println!("error");
            } else if find_v {
                println!("V = {:.6}", n * R * t.unwrap() / p);
            } else {
                println!("T = {:.6}", p * v.unwrap() / (n * R));
            }
        }
        _ => {}
    }
}
