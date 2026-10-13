use std::io::{self, Read};

const WIN: u32 = 3;
const DRAW: u32 = 1;

/// Tarjan's strongly connected components.
struct Tarjan<'a> {
    graph: &'a [Vec<usize>],
    idx: Vec<Option<usize>>,
    low: Vec<usize>,
    comp: Vec<usize>,
    stack: Vec<usize>,
    on_stack: Vec<bool>,
    counter: usize,
    comps: usize,
}

impl<'a> Tarjan<'a> {
    fn visit(&mut self, v: usize) {
        self.idx[v] = Some(self.counter);
        self.low[v] = self.counter;
        self.counter += 1;
        self.stack.push(v);
        self.on_stack[v] = true;
        let graph = self.graph;
        for &u in &graph[v] {
            match self.idx[u] {
                None => {
                    self.visit(u);
                    self.low[v] = self.low[v].min(self.low[u]);
                }
                Some(i) if self.on_stack[u] => self.low[v] = self.low[v].min(i),
                _ => {}
            }
        }
        if Some(self.low[v]) == self.idx[v] {
            loop {
                let u = self.stack.pop().unwrap();
                self.on_stack[u] = false;
                self.comp[u] = self.comps;
                if u == v {
                    break;
                }
            }
            self.comps += 1;
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i32> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let said: Vec<&[i32]> = v[1..].chunks(n).take(n).collect();
    // 2-SAT on "captain i tells the truth" (literal 2i) or lies (2i + 1),
    // and i scored against j exactly when the literal of statement (i, j) holds
    let literal = |i: usize, j: usize| if said[i][j] == 1 { 2 * i } else { 2 * i + 1 };
    let mut graph = vec![Vec::new(); 2 * n];
    for i in 0..n {
        for j in i + 1..n {
            if said[i][j] >= 0 && said[j][i] >= 0 {
                // somebody scores in every match: a or b, so not a -> b
                let (a, b) = (literal(i, j), literal(j, i));
                graph[a ^ 1].push(b);
                graph[b ^ 1].push(a);
            }
        }
    }
    let mut t = Tarjan {
        graph: &graph,
        idx: vec![None; 2 * n],
        low: vec![0; 2 * n],
        comp: vec![0; 2 * n],
        stack: Vec::new(),
        on_stack: vec![false; 2 * n],
        counter: 0,
        comps: 0,
    };
    for v in 0..2 * n {
        if t.idx[v].is_none() {
            t.visit(v);
        }
    }
    if (0..n).any(|i| t.comp[2 * i] == t.comp[2 * i + 1]) {
        println!("Impossible");
        return;
    }
    // Tarjan numbers components in reverse topological order
    let truthful: Vec<bool> = (0..n).map(|i| t.comp[2 * i] < t.comp[2 * i + 1]).collect();
    let scored = |i: usize, j: usize| said[i][j] < 0 || (said[i][j] == 1) == truthful[i];
    let mut table = vec![vec![0u32; n]; n];
    for i in 0..n {
        for j in i + 1..n {
            match (scored(i, j), scored(j, i)) {
                (true, true) => {
                    table[i][j] = DRAW;
                    table[j][i] = DRAW;
                }
                (true, false) => table[i][j] = WIN,
                _ => table[j][i] = WIN,
            }
        }
    }
    let rows: Vec<String> = table
        .iter()
        .map(|row| {
            row.iter()
                .map(|x| x.to_string())
                .collect::<Vec<_>>()
                .join(" ")
        })
        .collect();
    println!("{}", rows.join("\n"));
}
