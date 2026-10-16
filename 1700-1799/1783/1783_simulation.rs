use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let n = words.next().unwrap() as usize;
    let m = words.next().unwrap() as usize;
    let plan: Vec<i64> = words.take(n + m - 1).collect();
    let mut stock = 0i64;
    let mut orders = Vec::with_capacity(n);
    for i in 0..n {
        // after t months of the same change x the stock is stock + t x, which
        // must reach the plan of that month; x is rounded up, also below zero
        let x = (1..=m)
            .map(|t| -(stock - plan[i + t - 1]).div_euclid(t as i64))
            .max()
            .unwrap();
        orders.push(x.to_string());
        stock += x;
    }
    println!("{}", orders.join(" "));
}
