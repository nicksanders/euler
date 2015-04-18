
fn main() {

    let sum_of_squares = (1..101).map(|n| n * n).fold(0, |sum, x| sum + x);

    let mut square_of_sum = (1..101).fold(0, |sum, x| sum + x);
    square_of_sum *= square_of_sum;

    println!("{}", square_of_sum - sum_of_squares);

}
