use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input.split_ascii_whitespace();
    let n: usize = tok.next().unwrap().parse().unwrap();
    // a turning pair "><" becomes "<>", a swap of neighbours that removes one
    // pair with '>' before '<', so the count of such pairs is the answer
    let (mut right, mut turns) = (0u64, 0u64);
    for c in tok.flat_map(|t| t.bytes()).take(n) {
        if c == b'>' {
            right += 1;
        } else if c == b'<' {
            turns += right;
        }
    }
    println!("{}", turns);
}
