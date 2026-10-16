use std::f64::consts::PI;
use std::io::{self, Read};

const GRAVITY: f64 = 9.81;
const CENTIMETRES: f64 = 100.0;
const SECONDS: f64 = 60.0;
const STEPS: usize = 100;
const TURN: usize = 4;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let [length, height, turns] = v[..] else {
        return;
    };
    let half = length / CENTIMETRES / 2.0;
    let top = height / CENTIMETRES;
    let omega = turns * 2.0 * PI / SECONDS;
    let quarter = PI / 2.0 / omega;
    // the height of the lowest end of the toast at time t
    let gap = |t: f64| top - GRAVITY * t * t / 2.0 - half * (omega * t).sin().abs();
    // d gap / dt in quarter k, where the angle within the half turn is
    // omega*t - (k / 2)*pi
    let slope =
        |t: f64, k: usize| -GRAVITY * t - half * omega * (omega * t - (k / 2) as f64 * PI).cos();
    // d slope / dt, falling through an odd quarter
    let bend = |t: f64, k: usize| {
        -GRAVITY + half * omega * omega * (omega * t - (k / 2) as f64 * PI).sin()
    };
    let mut k = 0;
    loop {
        let (a, b) = (k as f64 * quarter, (k + 1) as f64 * quarter);
        let mut lowest = gap(b);
        if k % 2 == 1 {
            // the end rises again here: the slope of the gap is concave, so
            // find its peak; where it turns positive, the gap has a minimum
            let (mut lo, mut hi) = (a, b);
            for _ in 0..STEPS {
                let mid = (lo + hi) / 2.0;
                if bend(mid, k) > 0.0 {
                    lo = mid;
                } else {
                    hi = mid;
                }
            }
            if slope(lo, k) > 0.0 {
                hi = lo;
                lo = a;
                for _ in 0..STEPS {
                    let mid = (lo + hi) / 2.0;
                    if slope(mid, k) < 0.0 {
                        lo = mid;
                    } else {
                        hi = mid;
                    }
                }
                lowest = lowest.min(gap(lo));
            }
        }
        if lowest <= 0.0 {
            break;
        }
        k += 1;
    }
    // in quarters 0 and 3 of a turn the butter faces down
    let in_turn = k % TURN;
    println!("{}", if in_turn == 0 || in_turn == TURN - 1 { "butter" } else { "bread" });
}
