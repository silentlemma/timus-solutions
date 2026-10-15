use std::io::{self, Read, Write};

const MOST: i64 = 1_000_000_000; // nobody but Vasily earns more; nobody earns less than 0
const FIELDS: usize = 3; // i j d

struct Dsu {
    parent: Vec<usize>,
    size: Vec<usize>,
    offset: Vec<i64>,
}

impl Dsu {
    fn find(&mut self, mut x: usize) -> usize {
        let mut path = Vec::new();
        while self.parent[x] != x {
            path.push(x);
            x = self.parent[x];
        }
        // compress: walk back from the node nearest to the root
        let mut total = 0;
        for &v in path.iter().rev() {
            total += self.offset[v];
            self.offset[v] = total;
            self.parent[v] = x;
        }
        x
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (n, m) = (v[0] as usize, v[1] as usize);
    // a weighted union-find: salary[x] = salary[root] + offset[x], and every
    // root keeps the range its own salary may take so that all salaries of
    // its set stay in [0, MOST]; Vasily (0) is pinned to 0
    let mut dsu = Dsu { parent: (0..n).collect(), size: vec![1; n], offset: vec![0; n] };
    let mut low = vec![0i64; n];
    let mut high = vec![MOST; n];
    high[0] = 0;
    for (k, s) in v[2..2 + FIELDS * m].chunks(FIELDS).enumerate() {
        let (i, j, d) = (s[0] as usize, s[1] as usize, s[2]);
        let (mut ri, mut rj) = (dsu.find(i), dsu.find(j));
        // salary[i] - salary[j] = d means salary[rj] = salary[ri] + shift
        let mut shift = dsu.offset[i] - dsu.offset[j] - d;
        let mut ok = shift == 0;
        if ri != rj {
            if dsu.size[ri] < dsu.size[rj] {
                std::mem::swap(&mut ri, &mut rj);
                shift = -shift;
            }
            // salary[rj] lies in [low[rj], high[rj]], so salary[ri] in that minus shift
            low[ri] = low[ri].max(low[rj] - shift);
            high[ri] = high[ri].min(high[rj] - shift);
            ok = low[ri] <= high[ri];
            dsu.parent[rj] = ri;
            dsu.offset[rj] = shift;
            dsu.size[ri] += dsu.size[rj];
        }
        if !ok {
            println!("Impossible after {} statements", k + 1);
            return;
        }
    }
    let mut out = String::from("Possible\n");
    for x in 0..n {
        let r = dsu.find(x);
        out.push_str(&(low[r] + dsu.offset[x]).to_string());
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
