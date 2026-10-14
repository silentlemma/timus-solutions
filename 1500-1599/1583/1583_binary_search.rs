use std::f64::consts::PI;
use std::io::{self, Read};

const AREA: f64 = 100.0; // the cross-section of the bar, 10 by 10 cm
const LENGTH: f64 = 100.0;
const PIECE: f64 = 500.0; // grams, at one gram per cubic centimetre
const MICRONS: f64 = 10000.0; // in a centimetre
const STEPS: usize = 100;
const CAP: f64 = 3.0; // a cap of height h has volume pi h^2 (3 r - h) / 3
const HALF: f64 = 0.5;
const FIELDS: usize = 4; // x, y, z and r of a hole

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let values: Vec<f64> = it.map(|w| w.parse().unwrap()).collect();
    // each hole as its centre along the bar and its radius
    let holes: Vec<(f64, f64)> = values
        .chunks(FIELDS)
        .take(n)
        .map(|h| (h[1], h[FIELDS - 1]))
        .collect();
    // the weight of the bar from its start to the mark at (in cm): the full
    // volume minus the part of every hole below the mark, a spherical cap of
    // height h with volume pi h^2 (3 r - h) / 3
    let cheese = |at: f64| {
        let mut weight = AREA * at;
        for &(centre, r) in &holes {
            let h = (at - (centre - r)).max(0.0).min(2.0 * r);
            weight -= PI * h * h * (CAP * r - h) / CAP;
        }
        weight
    };
    let mut cuts = Vec::new();
    let mut start: i64 = 0;
    while cheese(LENGTH) - cheese(start as f64 / MICRONS) >= PIECE {
        // the mark where the next piece reaches 500 grams, then rounded to the
        // micrometre grid; the next piece starts at the cut actually made
        let base = cheese(start as f64 / MICRONS);
        let (mut lo, mut hi) = (start as f64 / MICRONS, LENGTH);
        for _ in 0..STEPS {
            let mid = (lo + hi) / 2.0;
            if cheese(mid) - base < PIECE {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        start = (hi * MICRONS + HALF).floor() as i64;
        if start >= (LENGTH * MICRONS) as i64 {
            break;
        }
        cuts.push(start);
    }
    println!("{}", cuts.len());
    for c in cuts {
        println!("{}", c);
    }
}
