fn main() {
    const HEIGHT: usize = 6;
    const WIDTH: usize = 11;
    let grid: [&str; HEIGHT] = [
        ">?v........",
        ".>>.......v",
        "..@A+AB+B-<",
        "..B........",
        "..-........",
        ".^@A!#.....",
    ];
    println!("{} {}", HEIGHT, WIDTH);
    for row in grid {
        println!("{}", row);
    }
}
