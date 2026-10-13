use std::collections::{BTreeSet, HashMap};
use std::io::{self, Read};

const CELL: f64 = 1e-3; // distinct crossing points are at least this far apart
const SAME: f64 = 1e-4; // two estimates of one point are much closer than this
const FIELDS: usize = 3; // x, y and r of a cut

struct Points {
    xy: Vec<(f64, f64)>,
    grid: HashMap<(i64, i64), Vec<usize>>,
}

impl Points {
    fn id(&mut self, x: f64, y: f64) -> usize {
        let (cx, cy) = ((x / CELL).floor() as i64, (y / CELL).floor() as i64);
        for gx in cx - 1..=cx + 1 {
            for gy in cy - 1..=cy + 1 {
                if let Some(list) = self.grid.get(&(gx, gy)) {
                    for &p in list {
                        if (self.xy[p].0 - x).abs() < SAME && (self.xy[p].1 - y).abs() < SAME {
                            return p;
                        }
                    }
                }
            }
        }
        self.xy.push((x, y));
        self.grid
            .entry((cx, cy))
            .or_default()
            .push(self.xy.len() - 1);
        self.xy.len() - 1
    }
}

fn find(parent: &mut Vec<usize>, mut a: usize) -> usize {
    while parent[a] != a {
        parent[a] = parent[parent[a]];
        a = parent[a];
    }
    a
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let nums: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let n = nums[0] as usize;
    // a cut made twice is still one cut
    let circles: Vec<&[i64]> = nums[1..1 + FIELDS * n]
        .chunks(FIELDS)
        .collect::<BTreeSet<_>>()
        .into_iter()
        .collect();
    let k = circles.len();
    let mut parent: Vec<usize> = (0..k).collect();
    let mut points = Points {
        xy: Vec::new(),
        grid: HashMap::new(),
    };
    let mut on_circle: Vec<Vec<usize>> = vec![Vec::new(); k];
    for i in 0..k {
        let (x1, y1, r1) = (circles[i][0], circles[i][1], circles[i][2]);
        for j in i + 1..k {
            let (x2, y2, r2) = (circles[j][0], circles[j][1], circles[j][2]);
            let (dx, dy) = (x2 - x1, y2 - y1);
            let d2 = dx * dx + dy * dy;
            if d2 > (r1 + r2) * (r1 + r2) || d2 < (r1 - r2) * (r1 - r2) {
                continue; // apart, or one inside the other
            }
            // the crossings are p1 + (m * (dx, dy) +- sqrt(K) * (-dy, dx)) / (2 d2), K exact
            let m = d2 + r1 * r1 - r2 * r2;
            let root = (((2 * r1) * (2 * r1) * d2 - m * m) as f64).sqrt();
            for sign in [1.0, -1.0] {
                let x = x1 as f64 + ((m * dx) as f64 - sign * root * dy as f64) / (2 * d2) as f64;
                let y = y1 as f64 + ((m * dy) as f64 + sign * root * dx as f64) / (2 * d2) as f64;
                let p = points.id(x, y);
                on_circle[i].push(p);
                on_circle[j].push(p);
                if root == 0.0 {
                    break;
                }
            }
            let (a, b) = (find(&mut parent, i), find(&mut parent, j));
            parent[a] = b;
        }
    }
    // Euler's formula for a plane graph: faces = edges - vertices + components + 1,
    // a circle with no crossings counts as one vertex and one edge
    let mut edges = 0i64;
    let mut components = 0i64;
    for i in 0..k {
        on_circle[i].sort_unstable();
        on_circle[i].dedup();
        edges += on_circle[i].len() as i64;
        if find(&mut parent, i) == i {
            components += 1;
        }
    }
    println!("{}", edges - points.xy.len() as i64 + components + 1);
}
