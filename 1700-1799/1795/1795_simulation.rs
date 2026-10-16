use std::collections::{HashMap, VecDeque};
use std::io::{self, Read};

struct Customer {
    product: String,
    wanted: i32,
    seen: i32, // the amount told at the last visit, -1 before the first
}

// every description is three words: amount, "of", name
fn describe<'a>(it: &mut impl Iterator<Item = &'a str>) -> (String, i32) {
    let amount = it.next().unwrap().parse().unwrap();
    it.next();
    (it.next().unwrap().to_string(), amount)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let m: usize = it.next().unwrap().parse().unwrap();
    let mut stock: HashMap<String, i32> = (0..m).map(|_| describe(&mut it)).collect();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut line: VecDeque<Customer> = (0..n)
        .map(|_| {
            let (product, wanted) = describe(&mut it);
            Customer { product, wanted, seen: -1 }
        })
        .collect();
    let mut minutes = 0;
    while let Some(mut c) = line.pop_front() {
        minutes += 1;
        let left = stock.entry(c.product.clone()).or_insert(0);
        if *left >= c.wanted {
            *left -= c.wanted;
        } else if *left == c.seen {
            // the same rest as before the call: take it all
            *left = 0;
        } else if *left > 0 {
            // let the next one forward and call home; if the next one is
            // the last of the line, it is Mark's turn
            c.seen = *left;
            if line.is_empty() {
                break;
            }
            line.insert(1, c);
        }
    }
    println!("{}", minutes);
}
