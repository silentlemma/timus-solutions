use std::io::{self, Read};

// sin(1-sin(2+sin(3-...sin(n)...))): the sign after k is minus for odd k
fn sine(n: usize) -> String {
    let mut s = String::new();
    for k in 1..=n {
        s += &format!("sin({}", k);
        if k < n {
            s.push(if k % 2 == 1 { '-' } else { '+' });
        }
    }
    s + &")".repeat(n)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let mut out = "(".repeat(n - 1);
    for i in 1..=n {
        out += &format!("{}+{}", sine(i), n - i + 1);
        if i < n {
            out.push(')');
        }
    }
    println!("{}", out);
}
