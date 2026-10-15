use std::io::{self, Read};

fn find(parent: &mut [usize], mut x: usize) -> usize {
    let mut root = x;
    while parent[root] != root {
        root = parent[root];
    }
    while parent[x] != root {
        let next = parent[x];
        parent[x] = root;
        x = next;
    }
    root
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let k: u64 = text.trim().parse().unwrap();
    // roots[v]: the residues s with v + s * s = 0 (mod k), the residues of
    // the earlier numbers b joined to a number a = v by a + b * b = 0
    let mut roots: Vec<Vec<usize>> = vec![Vec::new(); k as usize];
    let mut written: Vec<Vec<usize>> = vec![Vec::new(); k as usize];
    for s in 0..k {
        roots[((k - s * s % k) % k) as usize].push(s as usize);
    }
    let mut parent: Vec<usize> = vec![0];
    for a in 1usize.. {
        parent.push(a);
        let r = a as u64 % k;
        let square = ((k - r * r % k) % k) as usize;
        let mut near = roots[r as usize].clone();
        if !near.contains(&square) {
            near.push(square);
        }
        for s in near {
            for &b in &written[s] {
                // every edge either joins two trees or closes the first cycle
                let (ra, rb) = (find(&mut parent, a), find(&mut parent, b));
                if ra == rb {
                    println!("{}", a);
                    return;
                }
                parent[rb] = ra;
            }
        }
        written[r as usize].push(a);
    }
}
