OFFSET = [8, 3, 0];

$fn=20;

module button_bracket () {
    difference () {
        hull () {
            cylinder (1, r=3, $fn=30);
            translate (OFFSET) cylinder (2.75, r=7, $fn=40);
        }
        translate ([0, 0, -1]) cylinder (10, r=3/2);
        hull () for (y=[0, -1]) for (x=[0, -1]) {
            translate ([x*10+1.4, y*10+1.6, 1]) cylinder (10, r=2);
        }
        for (x=[-1, 1]) for (y=[-1, 1]) translate (OFFSET+[x*6/2, y*8/2, -0.001]) {
            cylinder (10, r=.5);
            hull () {
                cylinder (1.5, r=0.5);
                translate ([0, y*.5, 0]) cylinder (1.25, r1=0.75, r2=0);
            }
        }
    }
}
