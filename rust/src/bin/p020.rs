
fn main() {

    let mut total = 0;
    let mut fact = (1..11).fold(1, |acc, x| acc * x);

    while fact > 0 {
        let x = fact % 10;
        total += x;
        fact = (fact - x) / 10;
    }

    println!("{}", total);

}
