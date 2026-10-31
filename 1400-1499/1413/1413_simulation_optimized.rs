use std::f64::consts::FRAC_1_SQRT_2 as HALF;
use std::io::{self, Read};

const KEYS: usize = 10;
// the numeric keypad: the jump of each key in steps east and north
const DX: [i64; KEYS] = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1];
const DY: [i64; KEYS] = [0, -1, -1, -1, 0, 0, 0, 1, 1, 1];

fn main() {
    // a refillable buffer avoids retaining up to a million input bytes.
    const BUFFER_SIZE: usize = 4096;
    let mut buffer = [0u8; BUFFER_SIZE];
    let mut input = io::stdin().lock();
    let mut stopped = false;
    let mut times = [0i64; KEYS];
    loop {
        let n = input.read(&mut buffer).unwrap();
        if n == 0 {
            break;
        }
        for &c in &buffer[..n] {
            if c == b'0' {
                stopped = true;
            }
            if !stopped && c.is_ascii_digit() {
                times[(c - b'0') as usize] += 1;
            }
        }
    }
    // straight jumps add whole metres, diagonal ones 1/sqrt(2) on each axis
    let (mut sx, mut sy, mut dx, mut dy) = (0i64, 0i64, 0i64, 0i64);
    for k in 0..KEYS {
        if DX[k] != 0 && DY[k] != 0 {
            dx += DX[k] * times[k];
            dy += DY[k] * times[k];
        } else {
            sx += DX[k] * times[k];
            sy += DY[k] * times[k];
        }
    }
    let x = sx as f64 + dx as f64 * HALF;
    let y = sy as f64 + dy as f64 * HALF;
    println!("{:.10} {:.10}", x, y);
}
