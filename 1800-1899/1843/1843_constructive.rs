use std::collections::{HashMap, HashSet};
use std::io::{self, Read};

// front, back, down, up, left, right: face 2a + side lies on axis a
const FACES: &[u8] = b"FBDULR";
const SIDES: usize = FACES.len();
const AXES: usize = SIDES / 2;
// the axis other than a and b is AXIS_SUM - a - b
const AXIS_SUM: usize = AXES * (AXES - 1) / 2;
const INSIDE: u8 = b'.';
// quarter turns about the vertical and the front-back axis: the face at
// each letter's place comes from the place of the next letter, cyclically
const QUARTER_TURNS: [&[u8]; 2] = [b"FLBR", b"DLUR"];

type Turn = [usize; SIDES];
type Extents = [usize; AXES];

fn face(c: u8) -> usize {
    FACES.iter().position(|&f| f == c).unwrap()
}

// every turn: p puts the old face p[k] at place k, and the two quarter
// turns generate all 24
fn rotations() -> Vec<Turn> {
    let mut start: Turn = [0; SIDES];
    for (k, v) in start.iter_mut().enumerate() {
        *v = k;
    }
    let mut turns = Vec::new();
    for cycle in QUARTER_TURNS.iter() {
        let mut p = start;
        for i in 0..cycle.len() {
            p[face(cycle[i])] = face(cycle[(i + 1) % cycle.len()]);
        }
        turns.push(p);
    }
    let mut seen: HashSet<Turn> = HashSet::new();
    seen.insert(start);
    let mut all = vec![start];
    let mut todo = vec![start];
    while let Some(p) = todo.pop() {
        for q in &turns {
            let mut r = [0; SIDES];
            for k in 0..SIDES {
                r[k] = p[q[k]];
            }
            if seen.insert(r) {
                all.push(r);
                todo.push(r);
            }
        }
    }
    all
}

// the extents and colours of a turned piece, written as one string
fn turned(p: &Turn, dims: &Extents, colors: &[u8]) -> Vec<u8> {
    let mut s = Vec::new();
    for a in 0..AXES {
        s.extend_from_slice(dims[p[2 * a] / 2].to_string().as_bytes());
        s.push(b',');
    }
    for k in 0..SIDES {
        s.push(colors[p[k]]);
    }
    s
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    for _ in 0..AXES {
        it.next();
    }
    let box_colors = it.next().unwrap().as_bytes().to_vec();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut pieces: Vec<(Extents, Vec<u8>)> = Vec::with_capacity(n);
    for _ in 0..n {
        let mut dims = [0; AXES];
        for d in dims.iter_mut() {
            *d = it.next().unwrap().parse().unwrap();
        }
        pieces.push((dims, it.next().unwrap().as_bytes().to_vec()));
    }
    let turns = rotations();
    let canonical = |dims: &Extents, colors: &[u8]| {
        turns.iter().map(|p| turned(p, dims, colors)).min().unwrap()
    };
    let find = |colors: &[u8], c: u8| colors.iter().position(|&x| x == c);
    // the pieces on the edge along an axis carry the two box colours of the
    // faces before it on the other axes; their remaining extents are the
    // sections, the first one also coloured like the start face
    let mut cuts: Vec<Vec<usize>> = Vec::new();
    for axis in 0..AXES {
        let a = if axis == 0 { 1 } else { 0 };
        let b = AXIS_SUM - axis - a;
        let (mut first, mut middle, mut last) = (Vec::new(), Vec::new(), Vec::new());
        for (dims, colors) in &pieces {
            if let (Some(fa), Some(fb)) =
                (find(colors, box_colors[2 * a]), find(colors, box_colors[2 * b]))
            {
                let extent = dims[AXIS_SUM - fa / 2 - fb / 2];
                if find(colors, box_colors[2 * axis]).is_some() {
                    first.push(extent);
                } else if find(colors, box_colors[2 * axis + 1]).is_some() {
                    last.push(extent);
                } else {
                    middle.push(extent);
                }
            }
        }
        first.extend(middle);
        first.extend(last);
        cuts.push(first);
    }
    // middle sections may come in any order: the pieces are the same
    let mut groups: HashMap<Vec<u8>, Vec<usize>> = HashMap::new();
    for (i, (dims, colors)) in pieces.iter().enumerate() {
        groups.entry(canonical(dims, colors)).or_default().push(i);
    }
    let mut answer = vec![String::new(); n];
    let mut corner = [0usize; AXES];
    for i in 0..cuts[0].len() {
        corner[1] = 0;
        for j in 0..cuts[1].len() {
            corner[2] = 0;
            for k in 0..cuts[2].len() {
                let place = [i, j, k];
                let mut want = [0usize; AXES];
                let mut paint = Vec::with_capacity(SIDES);
                for axis in 0..AXES {
                    want[axis] = cuts[axis][place[axis]];
                    let start = place[axis] == 0;
                    let end = place[axis] == cuts[axis].len() - 1;
                    paint.push(if start { box_colors[2 * axis] } else { INSIDE });
                    paint.push(if end { box_colors[2 * axis + 1] } else { INSIDE });
                }
                let piece = groups.get_mut(&canonical(&want, &paint)).unwrap().pop().unwrap();
                let target = turned(&turns[0], &want, &paint);
                for p in &turns {
                    if turned(p, &pieces[piece].0, &pieces[piece].1) == target {
                        let (front, down) = (FACES[p[0]] as char, FACES[p[2]] as char);
                        answer[piece] =
                            format!("{} {} {} {} {}", front, down, corner[0], corner[1], corner[2]);
                        break;
                    }
                }
                corner[2] += want[2];
            }
            corner[1] += cuts[1][j];
        }
        corner[0] += cuts[0][i];
    }
    println!("{}", answer.join("\n"));
}
