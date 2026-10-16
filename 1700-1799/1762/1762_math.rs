use std::io::{self, Read};

fn gcd(x: i64, y: i64) -> i64 {
    if y == 0 {
        x
    } else {
        gcd(y, x % y)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let (n, m) = (words.next().unwrap(), words.next().unwrap());
    let (a, b) = (n - 1, m - 1);
    let g = gcd(a, b);
    // the walk takes lcm(a, b) steps and turns every tile it passes over, so
    // a tile passed twice ends up white again; in units of g the crossings
    // are the inner points (x, y) with x and y both odd or both even
    let steps = a / g * b;
    let (wide, tall) = (a / g, b / g);
    let crossings = (wide / 2) * (tall / 2) + ((wide - 1) / 2) * ((tall - 1) / 2);
    println!("{}", steps + 1 - 2 * crossings);
}
