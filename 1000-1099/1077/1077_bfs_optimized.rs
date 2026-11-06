use std::io::{self, BufWriter, Read, Write};

const CITIES: usize = 201;
const ROAD: u8 = 1;
const TREE: u8 = 2;

fn number(input: &mut impl Iterator<Item = u8>) -> usize {
    let first = input.find(|byte| byte.is_ascii_digit()).unwrap();
    let mut value = usize::from(first - b'0');
    for byte in input.take_while(u8::is_ascii_digit) {
        value = value * 10 + usize::from(byte - b'0');
    }
    value
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes().map(Result::unwrap);
    let (cities, mut tours) = (number(&mut input), number(&mut input));
    let mut edges = [[0u8; CITIES]; CITIES];
    for _ in 0..tours {
        let (a, b) = (number(&mut input), number(&mut input));
        edges[a][b] = ROAD;
        edges[b][a] = ROAD;
    }
    let mut depth = [0u8; CITIES];
    let mut parent = [0usize; CITIES];
    let mut queue = [0usize; CITIES];
    for root in 1..=cities {
        if depth[root] != 0 {
            continue;
        }
        depth[root] = 1;
        queue[0] = root;
        let (mut head, mut end) = (0, 1);
        while head < end {
            let u = queue[head];
            head += 1;
            for v in 1..=cities {
                if edges[u][v] == ROAD && depth[v] == 0 {
                    depth[v] = depth[u] + 1;
                    parent[v] = u;
                    edges[u][v] = TREE;
                    edges[v][u] = TREE;
                    queue[end] = v;
                    end += 1;
                    tours -= 1;
                }
            }
        }
    }

    let mut out = BufWriter::new(io::stdout().lock());
    writeln!(out, "{}", tours).unwrap();
    let (mut left, mut right) = ([0usize; CITIES], [0usize; CITIES]);
    for u in 1..=cities {
        for v in u + 1..=cities {
            if edges[u][v] != ROAD {
                continue;
            }
            // A non-tree road and the tree path between its ends form one tour.
            let (mut a, mut b) = (u, v);
            let (mut l, mut r) = (0, 0);
            while a != b {
                if depth[a] >= depth[b] {
                    left[l] = a;
                    l += 1;
                    a = parent[a];
                } else {
                    right[r] = b;
                    r += 1;
                    b = parent[b];
                }
            }
            left[l] = a;
            write!(out, "{}", l + r + 1).unwrap();
            for city in left[..=l].iter().chain(right[..r].iter().rev()) {
                write!(out, " {}", city).unwrap();
            }
            writeln!(out).unwrap();
        }
    }
    out.flush().unwrap();
}
