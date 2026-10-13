use std::io::{self, Read};

const BASE: u64 = 1_000_000_000; // nine decimal digits per limb

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: u64 = input.trim().parse().unwrap();
    // derangements: d(1) = 0 and d(k) = k d(k - 1) + (-1)^k, kept as limbs
    // from the lowest; d(k) >= 1 for k >= 2, so subtracting 1 never underflows
    let mut count: Vec<u64> = vec![0];
    for k in 2..=n {
        let mut carry = 0;
        for limb in count.iter_mut() {
            let cur = *limb * k + carry;
            *limb = cur % BASE;
            carry = cur / BASE;
        }
        while carry > 0 {
            count.push(carry % BASE);
            carry /= BASE;
        }
        let mut i = 0;
        if k % 2 == 0 {
            count[0] += 1;
            while count[i] == BASE {
                count[i] = 0;
                i += 1;
                if i == count.len() {
                    count.push(0);
                }
                count[i] += 1;
            }
        } else {
            while count[i] == 0 {
                count[i] = BASE - 1;
                i += 1;
            }
            count[i] -= 1;
            if count.len() > 1 && *count.last().unwrap() == 0 {
                count.pop();
            }
        }
    }
    let mut out = count.last().unwrap().to_string();
    for limb in count.iter().rev().skip(1) {
        out.push_str(&format!("{:09}", limb));
    }
    println!("{}", out);
}
