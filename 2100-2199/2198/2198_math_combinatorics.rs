use std::io::{self, Read};

const PADDING: usize = 3;
const MOD: i64 = 1000000007;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let edges = n - 1;
    let length = 2 * edges;
    let mut inverse = vec![0_i64; length + 2];
    let mut choose = vec![0_i64; length + PADDING];
    inverse[1] = 1;
    choose[0] = 1;
    for i in 1..=length {
        let value = i as i64;
        if i > 1 {
            inverse[i] = MOD - (MOD / value) * inverse[(MOD % value) as usize] % MOD;
        }
        choose[i] = choose[i - 1] * (length - i + 1) as i64 % MOD * inverse[i] % MOD;
    }

    // Contour walks are Dyck paths. Sum the counts whose maximum is at least h.
    // Reflection at levels -1 and h gives this second difference, with width h + 1.
    let mut answer = 0_i64;
    for width in 2..=edges + 1 {
        for offset in (width..=edges + 1).step_by(width) {
            let index = edges + offset;
            answer += choose[index - 1] - 2 * choose[index] + choose[index + 1];
        }
    }
    println!("{}", (answer % MOD + MOD) % MOD);
}
