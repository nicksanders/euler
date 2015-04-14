
fn main() {

    let mut prod = 0;

    'outer: for c in (333..999) {
        let mut b = c;
        while b > 1 {
            let a = 1000 - b - c;
            if (a * a) + (b * b) == c * c {
                prod = a * b * c;
                break 'outer;
            }
            b -= 1
        }
    }

    println!("{}", prod);
}
