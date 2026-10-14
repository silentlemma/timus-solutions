use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text
        .split_ascii_whitespace()
        .map(|w| w.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let mut cars: Vec<usize> = it.take(n).collect();
    let mut place = vec![0; n + 1];
    for (i, &car) in cars.iter().enumerate() {
        place[car] = i;
    }
    // cut 1..n into the fewest runs of numbers that already stand in order, and a
    // new run starts where car v + 1 stands before car v
    let mut run = vec![0usize; n + 1];
    for car in 2..=n {
        run[car] = run[car - 1] + usize::from(place[car] < place[car - 1]);
    }
    let mut passes = 0;
    while (1 << passes) <= run[n] {
        passes += 1;
    }
    let mut out = String::new();
    writeln!(out, "{}", passes).unwrap();
    for bit in 0..=passes {
        let line: Vec<String> = cars.iter().map(|c| c.to_string()).collect();
        writeln!(out, "{}", line.join(" ")).unwrap();
        if bit == passes {
            break;
        }
        // pass b sends the cars whose run number has bit b set to the right, and
        // like a radix sort from the low bit up, the passes leave the runs in order
        let (left, right): (Vec<usize>, Vec<usize>) =
            cars.iter().partition(|&&car| run[car] >> bit & 1 == 0);
        cars = left;
        cars.extend(right);
    }
    print!("{}", out);
}
