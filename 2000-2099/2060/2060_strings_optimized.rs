use std::io::{self, Read};

// Each endpoint count is at most 300000. A block of cumulative totals
// therefore wraps at most once in 32 bits.
const BLOCK: usize = 4096;
// A radius is at most 150000, so its upper two bits fit four per byte.
const LOW_BITS: usize = 16;
const PER_BYTE: usize = 4;
const HIGH_BITS: usize = 2;
const HIGH_MASK: u8 = 3;

struct Radii {
    low: Vec<u16>,
    high: Vec<u8>,
}

impl Radii {
    fn new(n: usize) -> Self {
        Self {
            low: vec![0; n],
            high: vec![0; (n + PER_BYTE - 1) / PER_BYTE],
        }
    }

    fn get(&self, index: usize) -> usize {
        let shift = (index % PER_BYTE) * HIGH_BITS;
        let high = (self.high[index / PER_BYTE] >> shift) & HIGH_MASK;
        (usize::from(high) << LOW_BITS) | usize::from(self.low[index])
    }

    fn set(&mut self, index: usize, radius: usize) {
        let shift = (index % PER_BYTE) * HIGH_BITS;
        let high = &mut self.high[index / PER_BYTE];
        *high = (*high & !(HIGH_MASK << shift)) | (((radius >> LOW_BITS) as u8) << shift);
        self.low[index] = radius as u16;
    }
}

fn manacher(word: &[u8], radii: &mut Radii, odd: bool, mut visit: impl FnMut(usize, usize)) {
    let parity = usize::from(odd);
    let mut left = 0;
    let mut end = 0;
    for center in 0..word.len() {
        let mut radius = if center < end {
            let mirror = left + end - center - parity;
            radii.get(mirror).min(end - center)
        } else {
            parity
        };
        while radius < center + parity
            && center + radius < word.len()
            && word[center + parity - radius - 1] == word[center + radius]
        {
            radius += 1;
        }
        radii.set(center, radius);
        if center + radius > end {
            left = center + parity - radius;
            end = center + radius;
        }
        visit(center, radius);
    }
}

fn solve(word: &[u8]) -> i64 {
    let n = word.len();
    if word.windows(2).all(|pair| pair[0] == pair[1]) {
        const BOUNDARY_TRIPLES_DIVISOR: i64 = 6;
        let n = n as i64;
        return (n + 1) * n * (n - 1) / BOUNDARY_TRIPLES_DIVISOR;
    }
    if n >= 2 && word[0] != word[1] && word.iter().zip(&word[2..]).all(|(a, b)| a == b) {
        let n = n as i64;
        return (1..n)
            .map(|left| ((left + 1) / 2) * ((n - left + 1) / 2))
            .sum();
    }
    // Store only the low 32 bits per endpoint and a full sum per block.
    let mut totals = vec![0u32; n + 1];
    let mut radii = Radii::new(n);
    for odd in [true, false] {
        manacher(word, &mut radii, odd, |center, radius| {
            totals[center] = totals[center].wrapping_add(1);
            totals[center + radius] = totals[center + radius].wrapping_sub(1);
        });
    }
    let mut ending = 0u32;
    let mut prefix = 0i64;
    let mut checkpoints = Vec::with_capacity(n / BLOCK + 1);
    for (i, value) in totals.iter_mut().enumerate() {
        ending = ending.wrapping_add(*value);
        if i % BLOCK == 0 {
            checkpoints.push(prefix);
        }
        *value = prefix as u32;
        prefix += i64::from(ending);
    }
    let prefix = |i: usize| {
        let anchor = checkpoints[i / BLOCK];
        anchor + i64::from(totals[i].wrapping_sub(anchor as u32))
    };
    // If a right palindrome starts at s, its contribution is the ending
    // count at s-1. Starts for one center form an interval.
    let mut answer = 0i64;
    for odd in [true, false] {
        let parity = usize::from(odd);
        manacher(word, &mut radii, odd, |center, radius| {
            let start = center + parity - radius;
            let end = center + parity;
            answer += prefix(end.saturating_sub(1)) - prefix(start.saturating_sub(1));
        });
    }
    answer
}

fn main() {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input).unwrap();
    println!("{}", solve(input.trim().as_bytes()));
}
