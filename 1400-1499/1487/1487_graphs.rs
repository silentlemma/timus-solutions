use std::io::{self, Read};

const WORD_BITS: usize = 64;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut winners = vec![Vec::new(); n];
    let mut indegree = vec![0usize; n];
    for i in 0..n {
        for (j, c) in it.next().unwrap().bytes().enumerate() {
            if c == b'1' {
                winners[i].push(j);
                indegree[j] += 1;
            }
        }
    }
    // stronger[v]: every team that is stronger than v, as a bit set; the
    // results are transitive, so the wins form an acyclic graph
    let words = (n + WORD_BITS - 1) / WORD_BITS;
    let mut stronger = vec![vec![0u64; words]; n];
    let mut queue: Vec<usize> = (0..n).filter(|&v| indegree[v] == 0).collect();
    let mut h = 0;
    while h < queue.len() {
        let v = queue[h];
        h += 1;
        for &u in &winners[v] {
            for w in 0..words {
                stronger[u][w] |= stronger[v][w];
            }
            stronger[u][v / WORD_BITS] |= 1 << (v % WORD_BITS);
            indegree[u] -= 1;
            if indegree[u] == 0 {
                queue.push(u);
            }
        }
    }
    // A plays better than B when no team stronger than B is stronger than A
    let q: usize = it.next().unwrap().parse().unwrap();
    let mut out = String::new();
    for _ in 0..q {
        let a: usize = it.next().unwrap().parse::<usize>().unwrap() - 1;
        let b: usize = it.next().unwrap().parse::<usize>().unwrap() - 1;
        let common = (0..words).any(|w| stronger[a][w] & stronger[b][w] != 0);
        out.push_str(if common { "No\n" } else { "YES\n" });
    }
    print!("{}", out);
}
