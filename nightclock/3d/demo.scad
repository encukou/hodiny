use <thingiverse-1933779-ESP8266Models.scad>;
use <hook.scad>;
use <button-bracket.scad>;

MCU_HOLE_W = 51;
MCU_HOLE_H = 25;

translate ([-25/2, 0, 1.75]) rotate ([0, 180, 0]) NodeMCU_LV3 (pins=1);
hook();
for (y=[-1, 1]) translate ([-25, y*MCU_HOLE_W/2, 3.5]) {
    rotate ([0, 180, 0]) scale ([1, y, 1]) button_bracket();
}
