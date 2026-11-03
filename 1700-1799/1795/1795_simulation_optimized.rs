use std::collections::HashMap;
use std::io::{self, Read};

#[derive(Clone, Copy)]
struct Customer {
    product: usize,
    wanted: i32,
    seen: i32,
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let m: usize = it.next().unwrap().parse().unwrap();
    // Keys borrow the immutable input: no cloned names in the simulation.
    let mut ids: HashMap<&str, usize> = HashMap::with_capacity(m);
    let mut stock = vec![0i32; m + 1];
    for id in 1..=m {
        stock[id] = it.next().unwrap().parse().unwrap();
        it.next();
        ids.insert(it.next().unwrap(), id);
    }
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut line = Vec::with_capacity(n);
    for _ in 0..n {
        let wanted = it.next().unwrap().parse().unwrap();
        it.next();
        let product = ids.get(it.next().unwrap()).copied().unwrap_or(0);
        line.push(Customer {
            product,
            wanted,
            seen: -1,
        });
    }
    let mut front = 0;
    let mut minutes = 0;
    while front < n {
        let customer = line[front];
        let left = stock[customer.product];
        minutes += 1;
        if left >= customer.wanted {
            stock[customer.product] = left - customer.wanted;
        } else if left == customer.seen {
            stock[customer.product] = 0;
        } else if left > 0 {
            line[front].seen = left;
            if front + 1 == n {
                break;
            }
            line.swap(front, front + 1);
            continue;
        }
        front += 1;
    }
    println!("{}", minutes);
}
