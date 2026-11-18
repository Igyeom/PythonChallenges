jun loop

ten2:
ld r3
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
jcn az y2
jcn an eleven2

eleven2:
ld r3
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
jcn az y2
jcn an twelve2

twelve2:
ld r3
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
jcn az y2
jcn an thirteen2

thirteen2:
ld r3
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
jcn az y2
jcn an fourteen2

fourteen2:
ld r3
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
jcn az y2
jcn an fifteen2

fifteen2:
ld r3
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
dac
jcn az y2
jcn an n2

loop:
jms $3f0
ld r2
xch r9
ld r3
xch r0
ld r2
jcn az final
xch r3
ldm 3
xch r2
jms $3e0
ld r0
xch r3
jun ten2

n2:
ldm 3
xch r2
jms $3e0
ld r9
jun loop

y2:
clc
ldm 7
add r3
xch r3
ldm 0
add r2
xch r2
jms $3e0
ld r9
jun loop


final:
nop
