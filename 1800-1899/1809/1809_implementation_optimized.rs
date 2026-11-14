use std::io::{self, Read};

const SIDE: i32 = 20;
const COUNT: usize = 4;
const STEPS: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];

type Cell = (i32, i32);

fn good(p: &[Cell; COUNT]) -> bool {
    let mut degree = [0; COUNT];
    for a in 0..COUNT {
        let (x, y) = p[a];
        if !(1..=SIDE).contains(&x) || !(1..=SIDE).contains(&y) {
            return false;
        }
        for b in 0..a {
            let (xx, yy) = p[b];
            if x == xx && y == yy {
                return false;
            }
            // Three points on one line give the middle point two visible
            // neighbors. Any valid line therefore has at most two points.
            if x == xx || y == yy {
                degree[a] += 1;
                degree[b] += 1;
                if degree[a] > 1 || degree[b] > 1 {
                    return false;
                }
            }
        }
    }
    degree == [1; COUNT]
}

// Comparisons with the kept potatoes are constant throughout each open gap.
fn representatives(mut fixed: [i32; COUNT - 1]) -> impl Iterator<Item = i32> {
    fixed.sort_unstable();
    let mut coords = [0; 2 * (COUNT - 1) + 1];
    let mut previous = 0;
    let mut count = 0;
    for coordinate in fixed {
        if coordinate == previous {
            continue;
        }
        if previous + 1 < coordinate {
            coords[count] = previous + 1;
            count += 1;
        }
        coords[count] = coordinate;
        count += 1;
        previous = coordinate;
    }
    if previous < SIDE {
        coords[count] = previous + 1;
        count += 1;
    }
    IntoIterator::into_iter(coords).take(count)
}

fn solve(start: [Cell; COUNT]) -> [Cell; COUNT] {
    if good(&start) {
        return start;
    }
    let mut p = start;
    for k in 0..COUNT {
        let mut kept = start.iter().enumerate().filter(|&(i, _)| i != k);
        let kept: [Cell; COUNT - 1] = std::array::from_fn(|_| *kept.next().unwrap().1);
        for x in representatives(kept.map(|c| c.0)) {
            for y in representatives(kept.map(|c| c.1)) {
                // The moved potato has to see one of the three kept potatoes.
                if !kept.iter().any(|&(a, b)| a == x || b == y) {
                    continue;
                }
                p[k] = (x, y);
                if good(&p) {
                    return p;
                }
            }
        }
        p[k] = start[k];
    }
    // two moves always do: next to the two kept potatoes, or as a pair of
    // their own in rows and columns nobody else uses
    for k in 0..COUNT {
        for l in k + 1..COUNT {
            let mut fixed = (0..COUNT).filter(|&i| i != k && i != l).map(|i| start[i]);
            let kept = [fixed.next().unwrap(), fixed.next().unwrap()];
            let near = kept.map(|(x, y)| STEPS.map(|(dx, dy)| (x + dx, y + dy)));
            let mut p = start;
            for a in near.iter().flatten() {
                p[k] = *a;
                for b in near.iter().flatten() {
                    p[l] = *b;
                    if good(&p) {
                        return p;
                    }
                }
            }
            let used_x = |x: i32| kept.iter().any(|c| c.0 == x);
            let used_y = |y: i32| kept.iter().any(|c| c.1 == y);
            let fx = (1..).find(|&x| !used_x(x)).unwrap();
            let fy = (1..).find(|&y| !used_y(y) && !used_y(y + 1)).unwrap();
            p[k] = (fx, fy);
            p[l] = (fx, fy + 1);
            if good(&p) {
                return p;
            }
        }
    }
    unreachable!("a solution with at most two moves always exists");
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input.split_ascii_whitespace().map(|x| x.parse().unwrap());
    let start = std::array::from_fn(|_| (values.next().unwrap(), values.next().unwrap()));
    for (x, y) in solve(start) {
        println!("{} {}", x, y);
    }
}
