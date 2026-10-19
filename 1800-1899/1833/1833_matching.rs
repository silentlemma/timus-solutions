use std::io::{self, Read, Write};

const FREE: usize = usize::MAX;

struct Matching {
    adj: Vec<Vec<usize>>,
    match_left: Vec<usize>,
    match_right: Vec<usize>,
    stamp: Vec<usize>,
}

impl Matching {
    // Kuhn's augmenting search on the doubled graph: left copies and right
    // copies of the canoeists, adj[u] the right neighbours of left u
    fn augment(&mut self, u: usize, round: usize) -> bool {
        for i in 0..self.adj[u].len() {
            let v = self.adj[u][i];
            if self.stamp[v] == round {
                continue;
            }
            self.stamp[v] = round;
            let w = self.match_right[v];
            if w == FREE || self.augment(w, round) {
                self.match_left[u] = v;
                self.match_right[v] = u;
                return true;
            }
        }
        false
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<usize>().unwrap());
    let n = match it.next() {
        Some(v) => v,
        None => return,
    };
    let (k, m) = (it.next().unwrap(), it.next().unwrap());
    let mut adj = vec![Vec::new(); n];
    for _ in 0..m {
        let (a, b) = (it.next().unwrap() - 1, it.next().unwrap() - 1);
        adj[a].push(b);
        adj[b].push(a);
    }
    // each crew must get at least k between its two members; this linear
    // program has a half-integral optimum, k/2 for each copy of a canoeist
    // in a minimum vertex cover of the doubled bipartite graph
    let mut g = Matching {
        adj,
        match_left: vec![FREE; n],
        match_right: vec![FREE; n],
        stamp: vec![FREE; n],
    };
    for u in 0..n {
        g.augment(u, u);
    }
    // Konig: left copies unreachable from free left copies by alternating
    // paths, and right copies reachable, form a minimum cover
    let mut seen_left: Vec<bool> = g.match_left.iter().map(|&v| v == FREE).collect();
    let mut seen_right = vec![false; n];
    let mut queue: Vec<usize> = (0..n).filter(|&u| seen_left[u]).collect();
    let mut i = 0;
    while i < queue.len() {
        let u = queue[i];
        i += 1;
        for &v in &g.adj[u] {
            if seen_right[v] {
                continue;
            }
            seen_right[v] = true;
            let w = g.match_right[v];
            if w != FREE && !seen_left[w] {
                seen_left[w] = true;
                queue.push(w);
            }
        }
    }
    let mut out = String::new();
    for v in 0..n {
        let copies = (!seen_left[v]) as usize + seen_right[v] as usize;
        out.push_str(&format!("{:.1}\n", (copies * k) as f64 / 2.0));
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
