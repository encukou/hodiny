EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L esp8266:NodeMCU_1.0_(ESP-12E) U1
U 1 1 61687675
P 3000 3500
F 0 "U1" H 3000 4587 60  0000 C CNN
F 1 "NodeMCU_1.0_(ESP-12E)" H 3000 4481 60  0000 C CNN
F 2 "esp8266:NodeMCU1.0(12-E)" H 2400 2650 60  0001 C CNN
F 3 "" H 2400 2650 60  0000 C CNN
	1    3000 3500
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74HC595 U2
U 1 1 6168A2A1
P 5000 3300
F 0 "U2" H 5000 4081 50  0000 C CNN
F 1 "74HC595" H 5000 3990 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W7.62mm_Socket" H 5000 3300 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/sn74hc595.pdf" H 5000 3300 50  0001 C CNN
	1    5000 3300
	1    0    0    -1  
$EndComp
$Comp
L Display_Character:CC56-12EWA U3
U 1 1 6168D5D2
P 7250 3200
F 0 "U3" H 7250 3867 50  0000 C CNN
F 1 "CC56-12EWA" H 7250 3776 50  0000 C CNN
F 2 "Display_7Segment:CA56-12EWA" H 7250 2600 50  0001 C CNN
F 3 "http://www.kingbrightusa.com/images/catalog/SPEC/CA56-12EWA.pdf" H 6820 3230 50  0001 C CNN
	1    7250 3200
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_SPST SW1
U 1 1 6169B3DD
P 4850 1850
F 0 "SW1" H 4850 2085 50  0000 C CNN
F 1 "SW_SPST" H 4850 1994 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm_H13mm" H 4850 1850 50  0001 C CNN
F 3 "~" H 4850 1850 50  0001 C CNN
	1    4850 1850
	1    0    0    -1  
$EndComp
Wire Wire Line
	4100 1850 4650 1850
Wire Wire Line
	3800 3500 3950 3500
Text Label 3950 3600 0    50   ~ 0
dig2
Text Label 3950 3700 0    50   ~ 0
dig3
Text Label 3950 2900 0    50   ~ 0
dig4
Text Label 3950 2800 0    50   ~ 0
dig1
Wire Wire Line
	3800 3600 3950 3600
Wire Wire Line
	3950 3700 3800 3700
Wire Wire Line
	3800 2900 3950 2900
Text Label 8650 3300 0    50   ~ 0
dig1
Text Label 8650 3400 0    50   ~ 0
dig2
Text Label 8650 3500 0    50   ~ 0
dig3
Text Label 8650 3600 0    50   ~ 0
dig4
Wire Wire Line
	6150 2900 5400 2900
Text Label 3950 3800 0    50   ~ 0
ser
Text Label 4350 2900 0    50   ~ 0
ser
Text Label 3950 3000 0    50   ~ 0
rclk
Text Label 4350 3400 0    50   ~ 0
rclk
Text Label 3950 3100 0    50   ~ 0
button
Text Label 4100 1850 0    50   ~ 0
button
Text Label 3950 3200 0    50   ~ 0
srclk
Text Label 4350 3100 0    50   ~ 0
srclk
Wire Wire Line
	4350 2900 4600 2900
Wire Wire Line
	4600 3100 4350 3100
Wire Wire Line
	4600 3400 4350 3400
NoConn ~ 2200 2800
NoConn ~ 2200 2900
NoConn ~ 2200 3000
NoConn ~ 2200 3100
NoConn ~ 2200 3200
NoConn ~ 2200 3300
NoConn ~ 2200 3400
NoConn ~ 2200 3500
NoConn ~ 2200 3600
NoConn ~ 2200 3900
NoConn ~ 2200 4000
$Comp
L Device:R R1
U 1 1 616B375B
P 8500 3300
F 0 "R1" V 8293 3300 50  0000 C CNN
F 1 "R" V 8384 3300 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 8430 3300 50  0001 C CNN
F 3 "~" H 8500 3300 50  0001 C CNN
	1    8500 3300
	0    1    1    0   
$EndComp
$Comp
L Device:R R2
U 1 1 616B3C36
P 8500 3400
F 0 "R2" V 8293 3400 50  0000 C CNN
F 1 "R" V 8384 3400 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 8430 3400 50  0001 C CNN
F 3 "~" H 8500 3400 50  0001 C CNN
	1    8500 3400
	0    1    1    0   
$EndComp
$Comp
L Device:R R3
U 1 1 616B3F0D
P 8500 3500
F 0 "R3" V 8293 3500 50  0000 C CNN
F 1 "R" V 8384 3500 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 8430 3500 50  0001 C CNN
F 3 "~" H 8500 3500 50  0001 C CNN
	1    8500 3500
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 616B41A0
P 8500 3600
F 0 "R4" V 8293 3600 50  0000 C CNN
F 1 "R" V 8384 3600 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 8430 3600 50  0001 C CNN
F 3 "~" H 8500 3600 50  0001 C CNN
	1    8500 3600
	0    1    1    0   
$EndComp
Wire Wire Line
	5400 3000 6150 3000
Wire Wire Line
	6150 3100 5400 3100
Wire Wire Line
	5400 3200 6150 3200
Wire Wire Line
	6150 3400 5400 3400
Wire Wire Line
	5400 3300 6150 3300
Wire Wire Line
	6150 3500 5400 3500
Wire Wire Line
	5400 3600 6150 3600
NoConn ~ 5400 3800
$Comp
L power:GND #PWR0101
U 1 1 616BA218
P 5000 4000
F 0 "#PWR0101" H 5000 3750 50  0001 C CNN
F 1 "GND" H 5005 3827 50  0000 C CNN
F 2 "" H 5000 4000 50  0001 C CNN
F 3 "" H 5000 4000 50  0001 C CNN
	1    5000 4000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 616BB405
P 4200 3400
F 0 "#PWR0102" H 4200 3150 50  0001 C CNN
F 1 "GND" H 4205 3227 50  0000 C CNN
F 2 "" H 4200 3400 50  0001 C CNN
F 3 "" H 4200 3400 50  0001 C CNN
	1    4200 3400
	1    0    0    -1  
$EndComp
Text Label 3950 3500 0    50   ~ 0
srclr'
Text Label 4350 3200 0    50   ~ 0
srclr'
Wire Wire Line
	4350 3200 4600 3200
Wire Wire Line
	3950 3000 3800 3000
Wire Wire Line
	3800 3100 3950 3100
Wire Wire Line
	3950 3200 3800 3200
$Comp
L power:GND #PWR0103
U 1 1 616BF391
P 5050 1850
F 0 "#PWR0103" H 5050 1600 50  0001 C CNN
F 1 "GND" H 5055 1677 50  0000 C CNN
F 2 "" H 5050 1850 50  0001 C CNN
F 3 "" H 5050 1850 50  0001 C CNN
	1    5050 1850
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0104
U 1 1 616BF931
P 2000 4200
F 0 "#PWR0104" H 2000 4050 50  0001 C CNN
F 1 "+5V" H 2015 4373 50  0000 C CNN
F 2 "" H 2000 4200 50  0001 C CNN
F 3 "" H 2000 4200 50  0001 C CNN
	1    2000 4200
	1    0    0    -1  
$EndComp
Text Label 3950 3300 0    50   ~ 0
3v3
Text Label 5200 2700 0    50   ~ 0
3v3
Wire Wire Line
	5200 2700 5000 2700
Wire Wire Line
	3950 3800 3800 3800
Wire Wire Line
	3800 3300 3950 3300
Wire Wire Line
	4000 4100 3800 4100
Wire Wire Line
	2000 4200 2200 4200
$Comp
L power:GND #PWR0105
U 1 1 616C88E7
P 4600 3500
F 0 "#PWR0105" H 4600 3250 50  0001 C CNN
F 1 "GND" H 4605 3327 50  0000 C CNN
F 2 "" H 4600 3500 50  0001 C CNN
F 3 "" H 4600 3500 50  0001 C CNN
	1    4600 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	3800 2800 3950 2800
Wire Wire Line
	4200 3400 3800 3400
NoConn ~ 4000 4100
$EndSCHEMATC
