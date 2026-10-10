use std::collections::HashMap;
use std::fmt::Write;
use std::io::{self, Read};

const TRIANGLE: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let color = it.next().unwrap().as_bytes();
    let mut poly: Vec<usize> = (0..n).collect();
    let mut cuts = Vec::new();
    while poly.len() > TRIANGLE {
        let m = poly.len();
        let mut counts = HashMap::new();
        for &v in &poly {
            *counts.entry(color[v]).or_insert(0) += 1;
        }
        if let Some(k) = (0..m).find(|&k| counts[&color[poly[k]]] == 1) {
            // a color met once: every triangle of the fan from that vertex
            // has it plus two neighbouring vertices, which differ
            for j in 2..m - 1 {
                cuts.push((poly[k], poly[(k + j) % m]));
            }
            break;
        }
        // every color is met twice or more; a vertex whose neighbours differ
        // exists, as otherwise two colors would alternate around the whole
        // polygon, and cutting it off leaves all three colors
        let k = (0..m)
            .find(|&k| color[poly[(k + m - 1) % m]] != color[poly[(k + 1) % m]])
            .unwrap();
        cuts.push((poly[(k + m - 1) % m], poly[(k + 1) % m]));
        poly.remove(k);
    }
    let mut out = format!("{}\n", cuts.len());
    for (a, b) in cuts {
        writeln!(out, "{} {}", a + 1, b + 1).unwrap();
    }
    print!("{}", out);
}
