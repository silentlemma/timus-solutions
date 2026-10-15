use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|w| w.parse::<usize>().unwrap());
    let (n, k) = (it.next().unwrap(), it.next().unwrap());
    // the scale shows x times all the bars plus y - x times the platinum
    // ones, so the counts must have pairwise different subset sums; the
    // Conway-Guy sets u_n - u_i do, with the smallest largest count known
    let mut u: Vec<usize> = vec![0, 1];
    for m in 1..n {
        let r = ((2 * m) as f64).sqrt().round() as usize;
        u.push(2 * u[m] - u[m - r]);
    }
    if u[n] > k {
        println!("NO");
        return;
    }
    let counts: Vec<String> = (0..n).map(|i| (u[n] - u[i]).to_string()).collect();
    println!("YES\n{}", counts.join(" "));
}
