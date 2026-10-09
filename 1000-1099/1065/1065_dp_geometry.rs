use std::io::{self, Read};

type Point = (i64, i64);

fn cross(o: Point, a: Point, b: Point) -> i64 {
    (a.0 - o.0) * (b.1 - o.1) - (a.1 - o.1) * (b.0 - o.0)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let m = it.next().unwrap() as usize;
    let mut read = |count: usize| -> Vec<Point> {
        (0..count)
            .map(|_| (it.next().unwrap(), it.next().unwrap()))
            .collect()
    };
    let towers = read(n);
    let monuments = read(m);
    let dist: Vec<Vec<f64>> = towers
        .iter()
        .map(|a| {
            towers
                .iter()
                .map(|b| ((a.0 - b.0) as f64).hypot((a.1 - b.1) as f64))
                .collect()
        })
        .collect();
    let mut best = f64::INFINITY;
    if m == 0 {
        // any convex border contains a triangle of its towers that is not
        // longer, so the best border is the shortest triangle with an area
        for i in 0..n {
            for j in i + 1..n {
                for k in j + 1..n {
                    if cross(towers[i], towers[j], towers[k]) != 0 {
                        best = best.min(dist[i][j] + dist[j][k] + dist[k][i]);
                    }
                }
            }
        }
    } else {
        // the border goes clockwise, so the inside is on the right of every
        // side: a side i -> j may be used when all monuments are strictly right
        let ok: Vec<Vec<bool>> = (0..n)
            .map(|i| {
                (0..n)
                    .map(|j| {
                        i != j
                            && monuments
                                .iter()
                                .all(|&p| cross(towers[i], towers[j], p) < 0)
                    })
                    .collect()
            })
            .collect();
        // a monument inside rules out degenerate borders; from every first
        // tower, the shortest way around through towers in their order
        for s in 0..n {
            let mut way = vec![f64::INFINITY; n];
            way[s] = 0.0;
            for step in 1..n {
                let k = (s + step) % n;
                for back in 0..step {
                    let j = (s + back) % n;
                    if ok[j][k] {
                        way[k] = way[k].min(way[j] + dist[j][k]);
                    }
                }
                if ok[k][s] {
                    best = best.min(way[k] + dist[k][s]);
                }
            }
        }
    }
    println!("{:.2}", best);
}
