use std::io::{self, Read, Write};

const TWO: i32 = 2;
const THREE: i32 = 3;
const LIMB: u64 = 1_000_000_000; // nine decimal digits per limb
const TWOS_PER_STEP: u32 = 29; // 2^29 < LIMB
const THREES_PER_STEP: u32 = 18; // 3^18 < LIMB

/// Multiplies the little-endian number by base^exponent.
fn multiply_power(number: &mut Vec<u64>, base: u64, mut exponent: u32, per_step: u32) {
    while exponent > 0 {
        let step = exponent.min(per_step);
        let factor = base.pow(step);
        let mut carry = 0;
        for limb in number.iter_mut() {
            let cur = *limb * factor + carry;
            *limb = cur % LIMB;
            carry = cur / LIMB;
        }
        if carry > 0 {
            number.push(carry);
        }
        exponent -= step;
    }
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s
        .split_ascii_whitespace()
        .map(|x| x.parse::<i32>().unwrap());
    let n = match it.next() {
        Some(v) => v as usize,
        None => return,
    };
    let marks: Vec<i32> = it.take(n).collect();
    // a nonzero product is +-2^a 3^b: prefix counts of twos and threes
    let mut twos = vec![0u32; n + 1];
    let mut threes = vec![0u32; n + 1];
    for (i, &x) in marks.iter().enumerate() {
        twos[i + 1] = twos[i] + (x.abs() == TWO) as u32;
        threes[i + 1] = threes[i] + (x.abs() == THREE) as u32;
    }
    let key = |a: u32, b: u32| a as f64 * (TWO as f64).ln() + b as f64 * (THREE as f64).ln();
    let mut best: Option<(u32, u32)> = None; // the exponents of the best positive product
    let mut i = 0;
    while i < n {
        if marks[i] == 0 {
            i += 1;
            continue;
        }
        // a run without zeros: |x| >= 1, so longer runs never shrink the size
        let mut j = i;
        while j < n && marks[j] != 0 {
            j += 1;
        }
        let negatives: Vec<usize> = (i..j).filter(|&k| marks[k] < 0).collect();
        let spans = if negatives.len() % 2 == 0 {
            vec![(i, j)]
        } else {
            // drop the part up to the first negative or from the last one
            vec![(negatives[0] + 1, j), (i, negatives[negatives.len() - 1])]
        };
        for (lo, hi) in spans {
            if lo >= hi {
                continue;
            }
            let ab = (twos[hi] - twos[lo], threes[hi] - threes[lo]);
            if best.map_or(true, |b| key(ab.0, ab.1) > key(b.0, b.1)) {
                best = Some(ab);
            }
        }
        i = j;
    }
    let out = io::stdout();
    let mut out = out.lock();
    match best {
        Some((a, b)) => {
            let mut number = vec![1u64];
            multiply_power(&mut number, TWO as u64, a, TWOS_PER_STEP);
            multiply_power(&mut number, THREE as u64, b, THREES_PER_STEP);
            let mut text = number[number.len() - 1].to_string();
            for limb in number.iter().rev().skip(1) {
                text.push_str(&format!("{:09}", limb));
            }
            writeln!(out, "{}", text).unwrap();
        }
        // all marks are zeros or lone negatives
        None => writeln!(out, "{}", if marks.contains(&0) { 0 } else { marks[0] }).unwrap(),
    }
}
