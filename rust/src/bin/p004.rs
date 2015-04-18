
fn is_palindrome(n: u64) -> bool {
    let (mut reversed, mut tmp) = (0, n);

    while tmp != 0 {
        reversed = 10 * reversed + tmp % 10;
        tmp /= 10;
    }

    reversed == n
}

fn main() {

    let mut max_product = 0;

    for i in (100..999) {
        for j in (100..i) {
            let product = i * j;
            // if product.to_string() == product.to_string().chars().rev().collect::<String>() {
            //     if product > max_product {
            //         max_product = product;
            //     }
            // }
            if is_palindrome(product) && product > max_product {
                max_product = product;
            }
        }
    }

    println!("{}", max_product);

}
