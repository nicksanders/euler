
fn calc_sum_at_row(mut rows: Vec<Vec<usize>>, row_num: usize) -> usize {

    for i in (0..rows[row_num].len()) {
        rows[row_num][i] += *[rows[row_num + 1][i], rows[row_num + 1][i + 1]].iter().max().unwrap();
    }

    if rows[row_num].len() == 1 {
        return rows[row_num][0];
    } else {
        return calc_sum_at_row(rows.clone(), row_num - 1);
    }
}


fn main() {

    let rows = vec![
        vec![75],
        vec![95, 64],
        vec![17, 47, 82],
        vec![18, 35, 87, 10],
        vec![20, 4, 82, 47, 65],
        vec![19, 1, 23, 75, 3, 34],
        vec![88, 2, 77, 73, 7, 63, 67],
        vec![99, 65, 4, 28, 6, 16, 70, 92],
        vec![41, 41, 26, 56, 83, 40, 80, 70, 33],
        vec![41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        vec![53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        vec![70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        vec![91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        vec![63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        vec![4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ];

    let row_num = rows.len() - 2;

    println!("{}", calc_sum_at_row(rows, row_num));

}
