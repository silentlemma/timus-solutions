use std::collections::HashMap;
use std::io::{self, Read, Write};

const ROWS: usize = 3;
const FRONTIER: usize = 2 * ROWS;
const CELLS: usize = FRONTIER + ROWS;
const MASKS: usize = 1 << ROWS;
const GAIN: i32 = ROWS as i32 - 1;
const UNREACHABLE: i32 = -1;
const UNSET: usize = usize::MAX;
type State = [i32; FRONTIER];
const EMPTY: State = [0; FRONTIER];
const FINISHED: State = [-1; FRONTIER];

struct Edge {
    target: usize,
    mask: usize,
    weight: i32,
}

struct Layer {
    previous: Vec<usize>,
    masks: Vec<usize>,
}

fn root(parent: &mut [usize; CELLS], mut v: usize) -> usize {
    while v != parent[v] {
        parent[v] = parent[parent[v]];
        v = parent[v];
    }
    v
}

fn transition(state: &State, mask: usize) -> Option<State> {
    let mut parent = std::array::from_fn(|i| i);
    for i in 0..FRONTIER {
        for j in 0..i {
            if state[i] != 0 && state[i] == state[j] {
                let a = root(&mut parent, i);
                let b = root(&mut parent, j);
                parent[a] = b;
            }
        }
    }
    let mut active = [false; CELLS];
    for i in 0..FRONTIER {
        active[i] = state[i] != 0;
    }
    for r in 0..ROWS {
        active[FRONTIER + r] = mask >> r & 1 != 0;
    }
    for r in 0..ROWS {
        if !active[FRONTIER + r] {
            continue;
        }
        for c in 0..2 {
            for s in 0..ROWS {
                let old = c * ROWS + s;
                if r.abs_diff(s) != c + 1 || !active[old] {
                    continue;
                }
                let a = root(&mut parent, old);
                let b = root(&mut parent, FRONTIER + r);
                if a == b {
                    return None;
                }
                parent[a] = b;
            }
        }
    }
    let mut old_roots = [false; CELLS];
    let mut new_roots = [false; CELLS];
    for i in 0..CELLS {
        if active[i] {
            let representative = root(&mut parent, i);
            if i < ROWS {
                old_roots[representative] = true;
            } else {
                new_roots[representative] = true;
            }
        }
    }
    if (0..CELLS).any(|i| old_roots[i] && !new_roots[i]) {
        if !new_roots.iter().any(|&v| v) && old_roots.iter().filter(|&&v| v).count() == 1 {
            return Some(FINISHED);
        }
        return None;
    }
    let mut labels = [0; CELLS];
    let mut result = [0; FRONTIER];
    let mut count = 0;
    for i in ROWS..CELLS {
        if active[i] {
            let representative = root(&mut parent, i);
            if labels[representative] == 0 {
                count += 1;
                labels[representative] = count;
            }
            result[i - ROWS] = labels[representative];
        }
    }
    Some(result)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let mut states = vec![EMPTY, FINISHED];
    let mut indices = HashMap::from([(EMPTY, 0), (FINISHED, 1)]);
    let mut edges = Vec::new();
    let mut i = 0;
    while i < states.len() {
        let state = states[i];
        let mut outgoing = Vec::new();
        if state == FINISHED {
            outgoing.push(Edge {
                target: i,
                mask: 0,
                weight: 0,
            });
        } else {
            for mask in 0..MASKS {
                if state == EMPTY && mask == 0 {
                    continue;
                }
                if let Some(target) = transition(&state, mask) {
                    let id = *indices.entry(target).or_insert_with(|| {
                        let id = states.len();
                        states.push(target);
                        id
                    });
                    outgoing.push(Edge {
                        target: id,
                        mask,
                        weight: mask.count_ones() as i32,
                    });
                }
            }
        }
        edges.push(outgoing);
        i += 1;
    }
    let size = states.len();
    let mut scores = vec![UNREACHABLE; size];
    scores[0] = 0;
    let mut history = Vec::new();
    let mut stable = false;
    while history.len() < n && !stable {
        let mut following = vec![UNREACHABLE; size];
        let mut layer = Layer {
            previous: vec![UNSET; size],
            masks: vec![0; size],
        };
        for source in 0..size {
            if scores[source] == UNREACHABLE {
                continue;
            }
            for edge in &edges[source] {
                let candidate = scores[source] + edge.weight;
                if candidate > following[edge.target] {
                    following[edge.target] = candidate;
                    layer.previous[edge.target] = source;
                    layer.masks[edge.target] = edge.mask;
                }
            }
        }
        // An equal score shift is preserved by every subsequent DP step.
        stable = (0..size).all(|i| {
            scores[i] == UNREACHABLE && following[i] == UNREACHABLE
                || scores[i] != UNREACHABLE && following[i] == scores[i] + GAIN
        });
        scores = following;
        history.push(layer);
    }
    let mut best = UNREACHABLE;
    let mut vertex = 0;
    for i in 0..size {
        if (states[i] == FINISHED || states[i].iter().copied().max() == Some(1)) && scores[i] > best
        {
            best = scores[i];
            vertex = i;
        }
    }
    let mut board = vec![0; n];
    for column in (0..n).rev() {
        let layer = &history[column.min(history.len() - 1)];
        board[column] = layer.masks[vertex];
        vertex = layer.previous[vertex];
    }
    let mut output = Vec::with_capacity(2 * ROWS * n);
    for row in 0..ROWS {
        for (column, &mask) in board.iter().enumerate() {
            if column != 0 {
                output.push(b' ');
            }
            output.push(b'0' + (mask >> row & 1) as u8);
        }
        output.push(b'\n');
    }
    io::stdout().write_all(&output).unwrap();
}
