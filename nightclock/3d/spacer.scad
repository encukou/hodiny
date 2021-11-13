$fn=40;

difference () {
    cylinder (4, r=5);
    translate ([0, 0, -1]) cylinder (6, r=3/2+.25);
    translate ([3, -5, -1]) cube ([10, 10, 10]);
}

translate ([10, 0, 0]) difference () {
    cylinder (4, r=5);
    translate ([0, 0, -1]) cylinder (6, r=3/2+.25);
}
