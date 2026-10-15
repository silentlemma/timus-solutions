use std::io::{self, Read};

fn find(parent: &mut Vec<usize>, mut x: usize) -> usize {
    while parent[x] != x {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    x
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let d: i64 = words.next().unwrap().parse().unwrap();
    let a: i64 = words.next().unwrap().parse().unwrap();
    let flights: Vec<&[u8]> = words.take(n).map(|w| w.as_bytes()).collect();
    let mut parent: Vec<usize> = (0..n).collect();
    // the result must be a spanning tree: keep a spanning forest of the
    // existing flights, cancel the rest, then join the trees with new flights
    let mut plan = vec![vec![b'0'; n]; n];
    let mut cost: i64 = 0;
    for i in 0..n {
        for j in i + 1..n {
            if flights[i][j] == b'1' {
                let (ri, rj) = (find(&mut parent, i), find(&mut parent, j));
                if ri != rj {
                    parent[ri] = rj;
                } else {
                    plan[i][j] = b'd';
                    plan[j][i] = b'd';
                    cost += d;
                }
            }
        }
    }
    for j in 1..n {
        let (r0, rj) = (find(&mut parent, 0), find(&mut parent, j));
        if r0 != rj {
            parent[rj] = r0;
            plan[0][j] = b'a';
            plan[j][0] = b'a';
            cost += a;
        }
    }
    let mut out = format!("{}\n", cost);
    for row in &plan {
        out.push_str(std::str::from_utf8(row).unwrap());
        out.push('\n');
    }
    print!("{}", out);
}
