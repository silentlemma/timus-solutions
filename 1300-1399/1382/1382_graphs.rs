use std::collections::HashMap;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    // variable i is true when friend i's first statement is the true one,
    // and literal 2 v means v while 2 v + 1 means not v
    let mut groups: HashMap<(u8, usize), Vec<usize>> = HashMap::new();
    let mut order = Vec::new(); // claims about one person or one card: at most one holds
    for i in 0..n {
        let (a, b, c) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
        for (k, lit) in [
            ((0, i + 1), 2 * i),
            ((1, a), 2 * i),
            ((0, b), 2 * i + 1),
            ((1, c), 2 * i + 1),
        ] {
            groups
                .entry(k)
                .or_insert_with(|| {
                    order.push(k);
                    Vec::new()
                })
                .push(lit);
        }
    }
    let mut count = n;
    let mut clauses = Vec::new(); // one of the two literals must hold
    for k in &order {
        // at most one: helper s_j means some of the first j members holds
        let mut prev: Option<usize> = None;
        for &lit in &groups[k] {
            let s = count;
            count += 1;
            clauses.push((lit ^ 1, 2 * s));
            if let Some(p) = prev {
                clauses.push((2 * p + 1, 2 * s));
                clauses.push((2 * p + 1, lit ^ 1));
            }
            prev = Some(s);
        }
    }
    let m = 2 * count;
    let mut graph = vec![Vec::new(); m];
    for &(x, y) in &clauses {
        graph[x ^ 1].push(y);
        graph[y ^ 1].push(x);
    }
    // Tarjan's components, numbered from the sinks up
    let (mut index, mut low, mut comp) = (vec![usize::MAX; m], vec![0; m], vec![0; m]);
    let mut on_stack = vec![false; m];
    let mut stack = Vec::new();
    let (mut counter, mut comps) = (0, 0);
    for root in 0..m {
        if index[root] != usize::MAX {
            continue;
        }
        let mut work = vec![(root, 0usize)];
        while let Some((v, mut k)) = work.pop() {
            if k == 0 {
                index[v] = counter;
                low[v] = counter;
                counter += 1;
                stack.push(v);
                on_stack[v] = true;
            } else {
                low[v] = low[v].min(low[graph[v][k - 1]]);
            }
            let mut descended = false;
            while k < graph[v].len() {
                let u = graph[v][k];
                k += 1;
                if index[u] == usize::MAX {
                    work.push((v, k));
                    work.push((u, 0));
                    descended = true;
                    break;
                }
                if on_stack[u] {
                    low[v] = low[v].min(index[u]);
                }
            }
            if !descended && low[v] == index[v] {
                loop {
                    let u = stack.pop().unwrap();
                    on_stack[u] = false;
                    comp[u] = comps;
                    if u == v {
                        break;
                    }
                }
                comps += 1;
            }
        }
    }
    // a literal holds when its component comes before its negation's
    let out: Vec<&str> = (0..n)
        .map(|i| {
            if comp[2 * i] < comp[2 * i + 1] {
                "1"
            } else {
                "2"
            }
        })
        .collect();
    println!("{}", out.join(" "));
}
