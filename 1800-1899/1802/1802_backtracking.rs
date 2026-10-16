use std::io::{self, Read, Write};

const FACES: usize = 6;
const TURNS: usize = 4;
const WORD: usize = 64;

struct Puzzle {
    n: usize,
    parts: Vec<Vec<Vec<usize>>>,
    // options[part][face]: the different masks of that part on that face
    options: Vec<Vec<Vec<Vec<u64>>>>,
    face_of: Vec<Option<usize>>,
    chosen: Vec<Vec<u64>>,
}

impl Puzzle {
    // the cell at depth k under row r, column c of a face; every face is the
    // bottom one turned by a rotation of the cube, so no part is mirrored
    fn cell_index(&self, face: usize, r: usize, c: usize, k: usize) -> usize {
        let n = self.n;
        let last = n - 1;
        let cells = [
            (k, r, c),
            (last - k, last - r, c),
            (r, last - k, c),
            (r, k, last - c),
            (r, c, k),
            (r, last - c, last - k),
        ];
        let (y, z, x) = cells[face];
        (y * n + z) * n + x
    }

    fn placement(&self, p: usize, face: usize, turns: usize) -> Vec<u64> {
        let n = self.n;
        let mut mask = vec![0u64; (n * n * n + WORD - 1) / WORD];
        for r in 0..n {
            for c in 0..n {
                let (mut rr, mut cc) = (r, c);
                for _ in 0..turns {
                    let keep = rr;
                    rr = cc;
                    cc = n - 1 - keep;
                }
                for k in 0..self.parts[p][r][c] {
                    let id = self.cell_index(face, rr, cc, k);
                    mask[id / WORD] |= 1 << (id % WORD);
                }
            }
        }
        mask
    }

    fn solve(&mut self, used: &[u64], free_faces: usize) -> bool {
        if free_faces == 0 {
            return true;
        }
        // fill next the face with the fewest ways left
        let mut best: Option<(usize, Vec<(usize, usize)>)> = None;
        for f in 0..FACES {
            if free_faces >> f & 1 == 0 {
                continue;
            }
            let mut ways = Vec::new();
            for p in 0..FACES {
                if self.face_of[p].is_some() {
                    continue;
                }
                for (i, m) in self.options[p][f].iter().enumerate() {
                    if m.iter().zip(used).all(|(a, b)| a & b == 0) {
                        ways.push((p, i));
                    }
                }
            }
            if ways.is_empty() {
                return false;
            }
            if best.as_ref().map_or(true, |(_, w)| ways.len() < w.len()) {
                best = Some((f, ways));
            }
        }
        let (face, ways) = best.unwrap();
        for (p, i) in ways {
            self.face_of[p] = Some(face);
            self.chosen[p] = self.options[p][face][i].clone();
            let next: Vec<u64> = used.iter().zip(&self.chosen[p]).map(|(a, b)| a | b).collect();
            if self.solve(&next, free_faces & !(1 << face)) {
                return true;
            }
            self.face_of[p] = None;
        }
        false
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let parts: Vec<Vec<Vec<usize>>> = (0..FACES)
        .map(|_| (0..n).map(|_| (0..n).map(|_| it.next().unwrap()).collect()).collect())
        .collect();
    let volume: Vec<usize> = parts.iter().map(|p| p.iter().flatten().sum()).collect();
    let mut puzzle = Puzzle {
        n,
        parts,
        options: vec![vec![Vec::new(); FACES]; FACES],
        face_of: vec![None; FACES],
        chosen: vec![Vec::new(); FACES],
    };
    for p in 0..FACES {
        for f in 0..FACES {
            for t in 0..TURNS {
                let m = puzzle.placement(p, f, t);
                if !puzzle.options[p][f].contains(&m) {
                    puzzle.options[p][f].push(m);
                }
            }
        }
    }
    // a turn of the whole cube brings the largest part onto face 0 unturned
    let anchor = (0..FACES).rev().max_by_key(|&p| volume[p]).unwrap();
    puzzle.face_of[anchor] = Some(0);
    puzzle.chosen[anchor] = puzzle.placement(anchor, 0, 0);
    let start = puzzle.chosen[anchor].clone();
    if !puzzle.solve(&start, ((1 << FACES) - 1) & !1) {
        println!("No");
        return;
    }
    let cells = n * n * n;
    let mut label = vec![0; cells];
    for p in 0..FACES {
        for (i, l) in label.iter_mut().enumerate() {
            if puzzle.chosen[p][i / WORD] >> (i % WORD) & 1 == 1 {
                *l = p + 1;
            }
        }
    }
    let mut out = String::from("Yes\n");
    for row in label.chunks(n) {
        let line: Vec<String> = row.iter().map(|v| v.to_string()).collect();
        out.push_str(&line.join(" "));
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
