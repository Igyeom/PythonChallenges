ld r1

increment:
inc r0
jcn an rightshift

rightshift:
clc
rar
jcn c1 increment
jcn az finish
jcn c0 rightshift

finish:
xch r0
dac
xch r0
