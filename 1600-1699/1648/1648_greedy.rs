use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (n, d) = (nums[0] as usize, nums[1]);
    // sell to everyone who can be served: by the end of month i at most
    // i * d yachts exist, so the running total of sales is capped there
    let mut sales = Vec::with_capacity(n);
    let mut total = 0i64;
    for (i, &a) in nums[2..2 + n].iter().enumerate() {
        let next = (total + a).min((i as i64 + 1) * d);
        sales.push(next - total);
        total = next;
    }
    // build every yacht as late as possible: going backwards, whatever a
    // month cannot build is built earlier and waits one month per boundary
    let (mut carry, mut storage) = (0i64, 0i64);
    for &sold in sales.iter().rev() {
        storage += carry;
        carry = (sold + carry - d).max(0);
    }
    println!("{} {}", total, storage);
}
