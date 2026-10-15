use std::f64::consts::PI;
use std::io::{self, Read};

const BITS: usize = 8; // bits of a character, the lowest first
const ONE_FREQ: f64 = 2.0; // a one is sin(2 pi k / t), a zero sin(4 pi k / t)
const ZERO_FREQ: f64 = 4.0;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let t: usize = words.next().unwrap().parse().unwrap();
    let samples: Vec<f64> = words.take(n).map(|w| w.parse().unwrap()).collect();
    // over a whole number of periods sin(2 pi k / t) and sin(4 pi k / t) are
    // orthogonal to each other and to a constant, so the correlation of a bit's
    // samples with each wave picks the wave that was sent
    let bits: Vec<u8> = samples
        .chunks(t)
        .map(|block| {
            let (mut one, mut zero) = (0.0, 0.0);
            for (k, &x) in block.iter().enumerate() {
                let angle = PI * k as f64 / t as f64;
                one += x * (ONE_FREQ * angle).sin();
                zero += x * (ZERO_FREQ * angle).sin();
            }
            (one > zero) as u8
        })
        .collect();
    let decoded: String = bits
        .chunks(BITS)
        .map(|byte| byte.iter().enumerate().fold(0u8, |c, (j, &b)| c | b << j) as char)
        .collect();
    println!("{}", decoded);
}
