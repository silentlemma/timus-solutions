use std::io::{self, Read};

const EDGE: i64 = 1_000_000_000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let k = v[1] as usize;
    let mut candles: Vec<(i64, i64)> = v[2..].chunks(2).map(|c| (c[0], c[1])).collect();
    candles.sort();
    // take the first k candles from the left, ties broken from below: all
    // columns left of candle k, and its own column up to it; the cut from it
    // to (x - 1, EDGE) leaves the rest of its column outside
    let (x, y) = candles[k - 1];
    let mut polygon = vec![(-EDGE, -EDGE), (x, -EDGE), (x, y)];
    if x - 1 > -EDGE {
        polygon.push((x - 1, EDGE));
    }
    polygon.push((-EDGE, EDGE));
    println!("{}", polygon.len());
    for (px, py) in polygon {
        println!("{} {}", px, py);
    }
}
