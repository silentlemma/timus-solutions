use std::io::{self, Read};

const SECONDS: f64 = 10.0;
// once a whole line is done with this certainty the rest of the sum is lost
// in rounding
const SURE: f64 = 1e-15;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let m = n - 2;
    // done[i]: the chance that i rockets between two launched ones are all
    // launched within the volleys counted so far; a stretch of i rockets
    // splits at a random one into stretches of l and i - 1 - l
    let mut done = vec![0.0f64; m + 1];
    done[0] = 1.0;
    let mut volleys = 0.0;
    for j in 1..=m {
        volleys += 1.0 - done[m];
        let before = done.clone();
        for i in 0..=m {
            done[i] = if i <= j {
                1.0
            } else {
                (0..i).map(|l| before[l] * before[i - 1 - l]).sum::<f64>() / i as f64
            };
        }
        if 1.0 - done[m] < SURE {
            break;
        }
    }
    println!("{:.11}", SECONDS * volleys);
}
