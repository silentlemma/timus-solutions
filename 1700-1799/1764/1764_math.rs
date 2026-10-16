use std::io::{self, Read};

const ROUTES: usize = 4;
const BRIDGES: usize = 6;
// each bridge lies on exactly two of the four routes, one pair per bridge,
// in the input order: Nizhny Novgorod, Kotelnich, Perm, Kazan, Vyatskiye
// Polyany, Sarapul
const PAIRS: [(usize, usize); BRIDGES] = [(0, 3), (0, 2), (2, 3), (1, 2), (1, 3), (0, 1)];

// determinant of a small integer matrix, expanded along the first row
fn det(rows: &[Vec<i64>]) -> i64 {
    let n = rows.len();
    if n == 1 {
        return rows[0][0];
    }
    let mut total = 0;
    for j in 0..n {
        if rows[0][j] == 0 {
            continue;
        }
        let minor: Vec<Vec<i64>> = rows[1..]
            .iter()
            .map(|r| r.iter().enumerate().filter(|&(c, _)| c != j).map(|(_, &v)| v).collect())
            .collect();
        let sign = if j % 2 == 1 { -1 } else { 1 };
        total += sign * rows[0][j] * det(&minor);
    }
    total
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let caps: Vec<i64> = input.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let mut cons: Vec<(Vec<i64>, i64)> = Vec::new();
    for (&(i, j), &cap) in PAIRS.iter().zip(&caps) {
        let mut a = vec![0; ROUTES];
        a[i] = 1;
        a[j] = 1;
        cons.push((a, cap));
    }
    for i in 0..ROUTES {
        let mut a = vec![0; ROUTES];
        a[i] = -1;
        cons.push((a, 0));
    }
    // the best plan is a corner where four constraints are tight; each
    // corner is solved exactly by Cramer's rule, as numerators over a
    // common positive denominator
    let total = cons.len();
    let (mut best_num, mut best_den, mut best) = (-1i64, 1i64, Vec::new());
    for mask in 0usize..1 << total {
        if mask.count_ones() as usize != ROUTES {
            continue;
        }
        let chosen: Vec<usize> = (0..total).filter(|&k| mask >> k & 1 == 1).collect();
        let matrix: Vec<Vec<i64>> = chosen.iter().map(|&k| cons[k].0.clone()).collect();
        let mut den = det(&matrix);
        if den == 0 {
            continue;
        }
        let mut nums: Vec<i64> = (0..ROUTES)
            .map(|c| {
                let mut swapped = matrix.clone();
                for (r, &k) in chosen.iter().enumerate() {
                    swapped[r][c] = cons[k].1;
                }
                det(&swapped)
            })
            .collect();
        if den < 0 {
            den = -den;
            nums.iter_mut().for_each(|v| *v = -*v);
        }
        let ok = cons
            .iter()
            .all(|(a, b)| a.iter().zip(&nums).map(|(x, v)| x * v).sum::<i64>() <= b * den);
        let sum: i64 = nums.iter().sum();
        if ok && sum * best_den > best_num * den {
            best_num = sum;
            best_den = den;
            best = nums;
        }
    }
    let out: Vec<String> = best
        .iter()
        .map(|&v| format!("{:.3}", v as f64 / best_den as f64))
        .collect();
    println!("{}", out.join(" "));
}
