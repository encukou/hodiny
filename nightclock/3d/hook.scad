
HANDLE_HEIGHT = 65;
MCU_HOLE_W = 51;

module box (sizes, centering=[1, 1, 1], extra_negative=[0, 0, 0]) {
    translate ([
        -sizes[0]*centering[0]/2-extra_negative[0],
        -sizes[1]*centering[1]/2-extra_negative[1],
        -sizes[2]*centering[2]/2-extra_negative[2],
    ]) {
        cube ([
            sizes[0]+extra_negative[0],
            sizes[1]+extra_negative[1],
            sizes[2]+extra_negative[2],
        ]);
    }
}

module hook () {
    difference () {
        hull () {
            for (y=[-1, 1]) translate ([0, y*MCU_HOLE_W/2, 0]) {
                for (x=[0, 1]) translate ([x*HANDLE_HEIGHT, 0, 0]) {
                    cylinder (1, r=2.5+x*4);
                }
                translate ([HANDLE_HEIGHT, 0, 10]) {
                    sphere (r=5);
                }
            }
        }
        translate ([0, 0, 1]) box ([HANDLE_HEIGHT*2, 200, 100], [1, 1, 0]);
        for (y=[-1, 1]) translate ([0, y*MCU_HOLE_W/2, -1]) {
            cylinder (10, r=3/2, $fn=20);
        }
        hull () {
            for (y=[-1, 1]) for (x=[-1, 1]) translate ([x*40, y*18, -1]) {
                cylinder (10, r=5);
            }
        }
    }
}
