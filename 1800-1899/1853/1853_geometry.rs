use std::io::{self, Read};

// the length of the trace while the source a and the receiver b move along
// the directions ua and ub for the time span
fn stretch(a_pos: (f64, f64), b_pos: (f64, f64), ua: (f64, f64), ub: (f64, f64), span: f64) -> f64 {
    let (dx, dy) = (b_pos.0 - a_pos.0, b_pos.1 - a_pos.1);
    let (vx, vy) = (ub.0 - ua.0, ub.1 - ua.1);
    let a = vx * vx + vy * vy;
    let m = dx * vy - dy * vx; // constant cross product of d(t) = b - a and v
    if a == 0.0 || m <= 0.0 {
        return 0.0;
    }
    // the trace point is a + lam(t) d(t), lam linear; its speed is
    // |r(t)| / sqrt(q(t)) for q(t) = |d(t)|^2 and a quadratic r(t)
    let lam0 = (ua.0 * dy - ua.1 * dx) / m;
    let lam1 = (ua.0 * vy - ua.1 * vx) / m;
    let h = dx * vx + dy * vy;
    let c = dx * dx + dy * dy;
    let b = 2.0 * h;
    let r2 = 2.0 * lam1 * a;
    let r1 = ua.0 * vx + ua.1 * vy + lam1 * (b + h) + lam0 * a;
    let r0 = ua.0 * dx + ua.1 * dy + lam1 * c + lam0 * h;
    // r = alpha q + beta q' + gamma, integrated term by term
    let alpha = 2.0 * lam1;
    let beta = (r1 - alpha * b) / (2.0 * a);
    let gamma = r0 - alpha * c - beta * b;
    let root_a = a.sqrt();
    let tail = alpha * m * m / (2.0 * a) + gamma;
    let primitive = |t: f64| {
        let q = (a * t * t + b * t + c).max(0.0);
        let slope = 2.0 * a * t + b;
        let bend = tail * (slope / (2.0 * m)).asinh() / root_a;
        (lam1 * slope / (2.0 * a) + 2.0 * beta) * q.sqrt() + bend
    };
    // the speed changes sign at the roots of r: the trace has a cusp there
    let mut roots: Vec<f64> = Vec::new();
    if r2 != 0.0 {
        let half = r1 / 2.0;
        let disc = half * half - r2 * r0;
        if disc > 0.0 {
            let s = disc.sqrt();
            roots = vec![(-half - s) / r2, (-half + s) / r2];
            roots.sort_by(|x, y| x.partial_cmp(y).unwrap());
        }
    } else if r1 != 0.0 {
        roots.push(-r0 / r1);
    }
    let mut cuts = vec![0.0];
    cuts.extend(roots.into_iter().filter(|&t| t > 0.0 && t < span));
    cuts.push(span);
    cuts.windows(2)
        .map(|w| {
            let mid = (w[0] + w[1]) / 2.0;
            let part = primitive(w[1]) - primitive(w[0]);
            if r2 * mid * mid + r1 * mid + r0 >= 0.0 {
                part
            } else {
                -part
            }
        })
        .sum()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<f64>().unwrap());
    let n = it.next().unwrap() as usize;
    let pts: Vec<(f64, f64)> = (0..n).map(|_| (it.next().unwrap(), it.next().unwrap())).collect();
    let d = it.next().unwrap();
    let size: Vec<f64> = (0..n)
        .map(|i| {
            let k = (i + 1) % n;
            (pts[k].0 - pts[i].0).hypot(pts[k].1 - pts[i].1)
        })
        .collect();
    let dir: Vec<(f64, f64)> = (0..n)
        .map(|i| {
            let k = (i + 1) % n;
            ((pts[k].0 - pts[i].0) / size[i], (pts[k].1 - pts[i].1) / size[i])
        })
        .collect();
    // the source starts at vertex 0; the receiver d further along the border
    let (mut j, mut left) = (0, d);
    while left >= size[j] {
        left -= size[j];
        j += 1;
    }
    let mut b = (pts[j].0 + dir[j].0 * left, pts[j].1 + dir[j].1 * left);
    let mut ahead = size[j] - left; // what is left of the receiver's edge
    let (mut i, mut a, mut behind, mut total) = (0, pts[0], size[0], 0.0);
    // walk from one corner event to the next, one of the two at a vertex
    while i < n {
        total += stretch(a, b, dir[i], dir[j], behind.min(ahead));
        if behind <= ahead {
            ahead -= behind;
            b = (b.0 + dir[j].0 * behind, b.1 + dir[j].1 * behind);
            i += 1;
            if i < n {
                a = pts[i];
                behind = size[i];
            }
            if ahead <= 0.0 {
                j = (j + 1) % n;
                b = pts[j];
                ahead = size[j];
            }
        } else {
            behind -= ahead;
            a = (a.0 + dir[i].0 * ahead, a.1 + dir[i].1 * ahead);
            j = (j + 1) % n;
            b = pts[j];
            ahead = size[j];
        }
    }
    println!("{:.10}", total);
}
