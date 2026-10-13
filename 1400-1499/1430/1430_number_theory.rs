use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace().map(|x| x.parse::<i64>().unwrap());
    let (mut a, mut b, n) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
    let swapped = a < b;
    if swapped {
        std::mem::swap(&mut a, &mut b);
    }
    // b items of price a can always become a items of price b, so x below b is enough,
    // with a >= b either b or n / a is at most sqrt(n)
    let (mut spent, mut bx, mut by) = (-1i64, 0i64, 0i64);
    let mut x = 0;
    while x <= (n / a).min(b - 1) && spent != n {
        let y = (n - x * a) / b;
        if x * a + y * b > spent {
            spent = x * a + y * b;
            bx = x;
            by = y;
        }
        x += 1;
    }
    if swapped {
        std::mem::swap(&mut bx, &mut by);
    }
    println!("{} {}", bx, by);
}
