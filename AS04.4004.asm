ld r0
jun add_ones

add_ones:
jcn az add_tens
inc r8
dac
jcn az add_tens
jcn an add_ones

add_tens:
ld r1
jcn az add_hundreds
clc
ldm 10
add r8
xch r8
ldm 0
add r9
xch r9
ld r1
dac
xch r1
ld r1
jcn az add_hundreds
jcn an add_tens

add_hundreds:
ld r2
jcn az add_thousands
clc
ldm 4
add r8
xch r8
ldm 6
add r9
xch r9
ldm 0
add r10
xch r10
ld r2
dac
xch r2
ld r2
jcn az add_thousands
jcn an add_hundreds

add_thousands:
ld r3
jcn az final
clc
ldm 8
add r8
xch r8
ldm 14
add r9
xch r9
ldm 3
add r10
xch r10
ldm 0
add r11
xch r11
ld r3
dac
xch r3
ld r3
jcn an add_thousands

final:
nop
