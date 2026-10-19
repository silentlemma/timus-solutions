use std::io::{self, Read, Write};

// drop repeated points and points in the middle of a straight run
fn straighten(points: &[(i64, i64)]) -> Vec<(i64, i64)> {
    let mut out: Vec<(i64, i64)> = Vec::new();
    for &p in points {
        if out.last() == Some(&p) {
            continue;
        }
        while out.len() >= 2 {
            let a = out[out.len() - 2];
            let b = out[out.len() - 1];
            let same_x = a.0 == b.0 && b.0 == p.0;
            let same_y = a.1 == b.1 && b.1 == p.1;
            if !same_x && !same_y {
                break;
            }
            out.pop();
        }
        out.push(p);
    }
    out
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let (w, h) = (v[0], v[1]);
    let mut it = v[2..].iter().copied();
    let (x, y, d) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
    let half = w * h / 2;
    // Finland always holds the column of cells along its coast, the
    // lighthouse, and a corridor of cells from the lighthouse to that column
    let right = w - 1 - x - d;
    if h + d * d + right > half {
        println!("Impossible");
        return;
    }
    let mut points: Vec<(i64, i64)> = Vec::new();
    if h + d * (w - 1 - x) <= half {
        // every row of Finland runs from some column to the coast; the area
        // still missing pushes rows west from the top down
        let mut extra = half - (h + d * (w - 1 - x));
        let mut cuts: Vec<(i64, i64)> = Vec::new();
        for &(top, bottom, column) in &[(h, y + d, w - 1), (y + d, y, x), (y, 0, w - 1)] {
            let rows = top - bottom;
            if rows == 0 {
                continue;
            }
            let full = if column > 1 { rows.min(extra / (column - 1)) } else { 0 };
            extra -= full * (column - 1);
            if full > 0 {
                cuts.push((full, 1));
            }
            if full < rows {
                let part = extra.min(column - 1);
                extra -= part;
                cuts.push((1, column - part));
                if full + 1 < rows {
                    cuts.push((rows - full - 1, column));
                }
            }
        }
        let mut level = h;
        points.push((cuts[0].1, h));
        for &(rows, column) in &cuts {
            points.push((column, level));
            points.push((column, level - rows));
            level -= rows;
        }
    } else {
        // the border goes round the lighthouse: Finland takes full corridor
        // rows at the top of the lighthouse rows and part of one more row
        let rest = half - (h + d * d + right);
        let (more, part) = (rest / right, rest % right);
        let level = y + d - 1 - more;
        points = vec![
            (w - 1, h),
            (w - 1, y + d),
            (x, y + d),
            (x, y),
            (x + d, y),
            (x + d, level),
            (w - 1 - part, level),
            (w - 1 - part, level - 1),
            (w - 1, level - 1),
            (w - 1, 0),
        ];
    }
    let points = straighten(&points);
    let mut out = String::new();
    out.push_str(&format!("{}\n", points.len()));
    for (px, py) in points {
        out.push_str(&format!("{} {}\n", px, py));
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
