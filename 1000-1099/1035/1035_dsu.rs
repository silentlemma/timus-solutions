use std::io::{self, Read};

fn find(parent: &mut [usize], mut v: usize) -> usize {
    while parent[v] != v {
        parent[v] = parent[parent[v]];
        v = parent[v];
    }
    v
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let m: usize = it.next().unwrap().parse().unwrap();
    // the vertices of the grid are (i, j) -> i * (m + 1) + j; balance[v] is the number
    // of front stitches minus the number of back stitches that end at v
    let width = m + 1;
    let vertices = (n + 1) * width;
    let mut parent: Vec<usize> = (0..vertices).collect();
    let mut balance = vec![0i64; vertices];
    let mut stitched = vec![false; vertices];
    for side in 0..2 {
        let sign = if side == 0 { 1 } else { -1 };
        for i in 0..n {
            let row = it.next().unwrap().as_bytes();
            for j in 0..m {
                let c = row[j];
                let ends = [
                    (i * width + j, (i + 1) * width + j + 1),
                    ((i + 1) * width + j, i * width + j + 1),
                ];
                let present = [c == b'\\' || c == b'X', c == b'/' || c == b'X'];
                for d in 0..2 {
                    if !present[d] {
                        continue;
                    }
                    let (a, b) = ends[d];
                    balance[a] += sign;
                    balance[b] += sign;
                    stitched[a] = true;
                    stitched[b] = true;
                    let (ra, rb) = (find(&mut parent, a), find(&mut parent, b));
                    parent[ra] = rb;
                }
            }
        }
    }
    // a group needs one thread per two unbalanced stitch ends, and at least one
    let mut ends = vec![0i64; vertices];
    let mut used = vec![false; vertices];
    for v in 0..vertices {
        if stitched[v] {
            let r = find(&mut parent, v);
            used[r] = true;
            ends[r] += balance[v].abs();
        }
    }
    let threads: i64 = (0..vertices)
        .filter(|&v| used[v])
        .map(|v| if ends[v] > 0 { ends[v] / 2 } else { 1 })
        .sum();
    println!("{}", threads);
}
