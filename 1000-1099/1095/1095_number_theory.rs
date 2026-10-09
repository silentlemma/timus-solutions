use std::io::{self, Read, Write};

const DIVISOR: u32 = 7;
const KEY: &str = "1234";

fn remainder_of(s: &str) -> u32 {
    s.bytes()
        .fold(0, |r, c| (r * 10 + (c - b'0') as u32) % DIVISOR)
}

fn permute(prefix: String, rest: String, out: &mut Vec<String>) {
    if rest.is_empty() {
        out.push(prefix);
        return;
    }
    for i in 0..rest.len() {
        let mut others = rest.clone();
        let c = others.remove(i);
        permute(format!("{}{}", prefix, c), others, out);
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    // the 24 orders of 1, 2, 3, 4 leave every remainder modulo 7
    let mut orders = Vec::new();
    permute(String::new(), KEY.to_string(), &mut orders);
    let mut out = String::new();
    for number in it.take(n) {
        let mut rest = number.to_string();
        for d in KEY.chars() {
            let at = rest.find(d).unwrap();
            rest.remove(at);
        }
        // zeros go to the end, where they do not change divisibility by 7
        let head: String = rest.chars().filter(|&c| c != '0').collect();
        let zeros = "0".repeat(rest.len() - head.len());
        for o in &orders {
            let candidate = format!("{}{}", head, o);
            if remainder_of(&candidate) == 0 {
                out.push_str(&candidate);
                out.push_str(&zeros);
                out.push('\n');
                break;
            }
        }
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
