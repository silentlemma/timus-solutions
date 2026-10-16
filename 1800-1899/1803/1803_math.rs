use std::io::{self, Read};

const LIMB_LIMIT: usize = 1_000_000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let (k, n) = (v[0], v[1]);
    // the numbers are kept in limbs of base k^m, the largest power of k up
    // to a million, and digit_sum[v] is the sum of the base-k digits of a limb
    let mut base = 1;
    while base <= LIMB_LIMIT / k {
        base *= k;
    }
    let mut digit_sum = vec![0u32; base];
    for v in 1..base {
        digit_sum[v] = digit_sum[v / k] + (v % k) as u32;
    }

    let mut cost = vec![1u32; n];
    let (mut a, mut b): (Vec<usize>, Vec<usize>) = (vec![1], vec![1]);
    for c in cost.iter_mut().skip(2) {
        // a, b = b, a + b, summing the digits on the way
        a.resize(b.len(), 0);
        let (mut sum, mut carry) = (0, 0);
        for (x, &y) in a.iter_mut().zip(b.iter()) {
            let mut v = *x + y + carry;
            carry = (v >= base) as usize;
            v -= carry * base;
            *x = v;
            sum += digit_sum[v];
        }
        if carry == 1 {
            a.push(1);
            sum += 1;
        }
        std::mem::swap(&mut a, &mut b);
        *c = sum;
    }
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_by_key(|&i| cost[i]);
    let line: Vec<String> = order.iter().map(|i| (i + 1).to_string()).collect();
    println!("{}", line.join(" "));
}
