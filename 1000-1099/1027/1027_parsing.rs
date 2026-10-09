use std::io::{self, Read};

// characters allowed inside an arithmetic expression besides the brackets
const EXPRESSION: &[u8] = b"=+-*/0123456789\r\n";

fn valid(s: &[u8]) -> bool {
    let mut depth = 0;
    let mut i = 0;
    while i < s.len() {
        if s[i..].starts_with(b"(*") {
            // a comment ends at the first *) after its opening pair
            match s[i + 2..].windows(2).position(|w| w == b"*)") {
                Some(end) => i += 2 + end + 2,
                None => return false,
            }
            continue;
        }
        match s[i] {
            b'(' => depth += 1,
            b')' => {
                if depth == 0 {
                    return false;
                }
                depth -= 1;
            }
            c if depth > 0 && !EXPRESSION.contains(&c) => return false,
            _ => {}
        }
        i += 1;
    }
    depth == 0
}

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    println!("{}", if valid(&input) { "YES" } else { "NO" });
}
