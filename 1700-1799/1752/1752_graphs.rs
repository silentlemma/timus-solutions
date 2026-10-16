use std::io::{self, Read, Write};

const NONE: usize = usize::MAX;

struct Tree {
    head: Vec<usize>,
    nxt: Vec<usize>,
    to: Vec<usize>,
    ask_head: Vec<usize>,
    ask_next: Vec<usize>,
    ask_dist: Vec<usize>,
    answer: Vec<usize>,
    path: Vec<usize>,
}

impl Tree {
    // walk the tree from root in preorder: when a vertex is reached, path holds
    // its ancestors by depth, so a query at it with d <= depth is answered at
    // once; returns the deepest vertex
    fn walk(&mut self, root: usize) -> usize {
        let mut depth = vec![NONE; self.head.len()];
        depth[root] = 0;
        let mut deepest = root;
        let mut stack = vec![root];
        while let Some(v) = stack.pop() {
            let dv = depth[v];
            self.path[dv] = v;
            if dv > depth[deepest] {
                deepest = v;
            }
            let mut i = self.ask_head[v];
            while i != NONE {
                if self.answer[i] == 0 && self.ask_dist[i] <= dv {
                    self.answer[i] = self.path[dv - self.ask_dist[i]];
                }
                i = self.ask_next[i];
            }
            let mut e = self.head[v];
            while e != NONE {
                let u = self.to[e];
                if depth[u] == NONE {
                    depth[u] = dv + 1;
                    stack.push(u);
                }
                e = self.nxt[e];
            }
        }
        deepest
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<usize>().unwrap());
    let n = words.next().unwrap();
    let q = words.next().unwrap();
    let mut t = Tree {
        head: vec![NONE; n + 1],
        nxt: Vec::with_capacity(2 * n),
        to: Vec::with_capacity(2 * n),
        ask_head: vec![NONE; n + 1],
        ask_next: vec![NONE; q],
        ask_dist: vec![0; q],
        answer: vec![0; q],
        path: vec![0; n + 1],
    };
    for _ in 1..n {
        let a = words.next().unwrap();
        let b = words.next().unwrap();
        t.to.push(b);
        t.nxt.push(t.head[a]);
        t.head[a] = t.to.len() - 1;
        t.to.push(a);
        t.nxt.push(t.head[b]);
        t.head[b] = t.to.len() - 1;
    }
    for i in 0..q {
        let v = words.next().unwrap();
        t.ask_dist[i] = words.next().unwrap();
        t.ask_next[i] = t.ask_head[v];
        t.ask_head[v] = i;
    }
    // the farthest vertex from any vertex is an end of a diameter, and the
    // walk from vertex 1 ends at one end, the walk from there at the other
    let a = t.walk(1);
    let b = t.walk(a);
    t.walk(b);
    let mut out = String::new();
    for x in &t.answer {
        out.push_str(&x.to_string());
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
