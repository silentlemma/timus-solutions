use std::io::{self, Read};

fn solve(south: &str, north: &str) -> usize {
    let (south, north) = (south.as_bytes(), north.as_bytes());
    let (mut i, mut j, mut elapsed) = (0, 0, 0);
    while i < south.len() && j < north.len() {
        let (a, b) = (south[i], north[j]);
        let go_a = a != b'L' || b == b'L';
        let go_b = b != b'L' || a == b'L';
        i += usize::from(go_a);
        j += usize::from(go_b);
        elapsed += 1;
    }
    elapsed + south.len() - i + north.len() - j
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let south = tokens.next().unwrap();
    let north = tokens.next().unwrap();
    println!("{}", solve(south, north));
}
