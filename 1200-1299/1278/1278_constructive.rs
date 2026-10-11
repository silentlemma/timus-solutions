use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let k: u64 = input.trim().parse().unwrap();
    // from the BELL&RET cell upwards: "CALL i + 1" at cell i doubles the
    // bells made from the next cell, a call of the last cell adds one more,
    // so the binary digits of K give the cells
    let mut doubles = Vec::new();
    for bit in format!("{:b}", k).bytes().skip(1) {
        doubles.push(true);
        if bit == b'1' {
            doubles.push(false);
        }
    }
    let last = doubles.len();
    let mut out = String::new();
    for cell in 0..last {
        let target = if doubles[last - 1 - cell] {
            cell + 1
        } else {
            last
        };
        out += &format!("CALL {}\n", target);
    }
    out += "BELL&RET";
    println!("{}", out);
}
