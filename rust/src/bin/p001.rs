
fn main() {
    println!("{}", (1..1000).filter(|&n| n % 3 == 0 || n % 5 == 0).fold(0, |sum, x| sum + x));
}
