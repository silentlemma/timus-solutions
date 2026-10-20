use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let s = tokens.next().unwrap().as_bytes();
    let zeros = s.iter().filter(|&&c| c == b'0').count();
    if n % 2 == 0 && zeros % 2 != 0 {
        println!("NO");
        return;
    }

    let mut balance = 0;
    for i in 0..n / 2 {
        // A zero can move left, so the suffix must supply at least as many zeros.
        balance += i32::from(s[n - 1 - i] == b'0') - i32::from(s[i] == b'0');
        if balance < 0 {
            println!("NO");
            return;
        }
    }
    println!("YES");
}
