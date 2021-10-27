import serial
import sys
from time import sleep
ser = serial.Serial('/dev/ttyUSB0')
print(ser.name) 

data = "*0000cafeffff0384ffff0284031400040007030f00af00040006000e0000f806fffef40600001e81fffc1f88006100040068030f0031000e0000f806fffef40600001e81fff61f8810000004fffca00600010004fffaa0060031000e00000004fff8a006002a000efffa1483006a00040000041cfff8148300002007000000070000000800000083fffc140300000406fffc140300020008fffca006fff8140300010008fff8a006fff81483006900040000040c001a028efffa140300010008fffaa006fffa1483002f00040000040c0017028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800010004fffca006005f000e00000004fffaa0060058000efffc1403ffff0108fffc1483006a00040000041cfffa148300002007000000070000000800000083006a00040000081cfffa150300004007000000070000000800000406fffa140300010008fffaa006fffa1483006900040000040c0044028efffc140300010008fffca006fffc1483002f00040000040c0041028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc150300ff091600ff091613e00082000800040000049913e2018213e1000200002894006a010400004d1c0000080700000007000000080000040613e100020001000813e1000513e10082006a00040000040c0090038e0000000413e1000513e200020001000813e2000513e20082003000040000040c0090038e003a030f000e030f0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc140300ff001600ff001613e000050000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f8840000004fffca006fffc140300010084000004060000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800000004fffca00600d2000e00000004fffaa00600cb000efffc1483006a00040000041cfffa14830000200700000007000000080000008400000406fffa140300010008fffaa006fffa1483006900040000040c00bf028efffc140300010008fffca006fffc1483002f00040000040c00bc028e00a7030f00ff000413e000050000000413e100050000000413e200050000000000001781fffe1e8300001f030000181100004845*"
data = "*0000cafeffff0384ffff0284031400040007030f00af00040006000e0000f806fffef40600001e81fffc1f88006100040068030f000b000e0000f806fffef40600001e81fff61f8810000004fffca00600010004fffaa0060031000e00000004fff8a006002a000efffa1483006a00040000041cfff8148300002007000000070000000800000083fffc140300000406fffc140300020008fffca006fff8140300010008fff8a006fff81483006900040000040c001a028efffa140300010008fffaa006fffa1483002f00040000040c0017028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800010004fffca006005f000e00000004fffaa0060058000efffc1403ffff0108fffc1483006a00040000041cfffa148300002007000000070000000800000083006a00040000081cfffa150300004007000000070000000800000406fffa140300010008fffaa006fffa1483006900040000040c0044028efffc140300010008fffca006fffc1483002f00040000040c0041028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc150300ff091600ff091613e00082000800040000049913e2018213e1000200002894006a010400004d1c0000080700000007000000080000040613e100020001000813e1000513e10082006a00040000040c0090038e0000000413e1000513e200020001000813e2000513e20082003000040000040c0090038e003a030f000e030f0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc140300ff001600ff001613e000050000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f8840000004fffca006fffc140300010084000004060000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800000004fffca00600d2000e00000004fffaa00600cb000efffc1483006a00040000041cfffa14830000200700000007000000080000008400000406fffa140300010008fffaa006fffa1483006900040000040c00bf028efffc140300010008fffca006fffc1483002f00040000040c00bc028e00a7030f00ff000413e000050000000413e100050000000413e200050000000000001781fffe1e8300001f03000018110000486b*"
data = "*0000cafeffff0384ffff0284031400040007030f00af00040006000e0000f806fffef40600001e81fffa1f8810000004fffca006fffc1403ff610084000004060000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff61f8810000004fffca00600010004fffaa0060038000e00000004fff8a0060031000efffa1483006a00040000041cfff8148300002007000000070000000800000083fffc140300000406fffc140300020008fffca006fff8140300010008fff8a006fff81483006900040000040c0021028efffa140300010008fffaa006fffa1483002f00040000040c001e028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800010004fffca0060066000e00000004fffaa006005f000efffc1403ffff0108fffc1483006a00040000041cfffa148300002007000000070000000800000083006a00040000081cfffa150300004007000000070000000800000406fffa140300010008fffaa006fffa1483006900040000040c004b028efffc140300010008fffca006fffc1483002f00040000040c0048028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc150300ff091600ff091613e00082000800040000049913e2018213e1000200002894006a010400004d1c0000080700000007000000080000040613e100020001000813e1000513e10082006a00040000040c0097038e0000000413e1000513e200020001000813e2000513e20082003000040000040c0097038e0041030f0015030f0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc140300ff001600ff001613e000050000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f8840000004fffca006fffc140300010084000004060000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800000004fffca00600d9000e00000004fffaa00600d2000efffc1483006a00040000041cfffa14830000200700000007000000080000008400000406fffa140300010008fffaa006fffa1483006900040000040c00c6028efffc140300010008fffca006fffc1483002f00040000040c00c3028e00ae030f00ff000413e000050000000413e100050000000413e200050000000000001781fffe1e8300001f0300001811000016e5*"
data = "*0000cafeffff0384ffff0284031400040007030f00af00040006000e0000f806fffef40600001e81fffa1f8810000004fffca006fffc14030f610084000004060000000000001781fffe1e8300001f03000018110000b8f4*"
data = "*0000cafeffff0384ffff0284031400040007030f00af00040006000e0000f806fffef40600001e81fffc1f88006100040068030f000b000e0000f806fffef40600001e81fff61f8810000004fffca00600010004fffaa0060031000e00000004fff8a006002a000efffa1483006a00040000041cfff8148300002007000000070000000800000083fffc140300000406fffc140300020008fffca006fff8140300010008fff8a006fff81483006900040000040c001a028efffa140300010008fffaa006fffa1483002f00040000040c0017028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800010004fffca006005f000e00000004fffaa0060058000efffc1403ffff0108fffc1483006a00040000041cfffa148300002007000000070000000800000083006a00040000081cfffa150300004007000000070000000800000406fffa140300010008fffaa006fffa1483006900040000040c0044028efffc140300010008fffca006fffc1483002f00040000040c0041028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc150300ff091600ff091613e00082000800040000049913e2018213e1000200002894006a010400004d1c0000080700000007000000080000040613e100020001000813e1000513e10082006a00040000040c0090038e0000000413e1000513e200020001000813e2000513e20082003000040000040c0090038e003a030f000e030f0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc140300ff001600ff001613e000050000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f8840000004fffca006fffc140300010084000004060000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800000004fffca00600d2000e00000004fffaa00600cb000efffc1483006a00040000041cfffa14830000200700000007000000080000008400000406fffa140300010008fffaa006fffa1483006900040000040c00bf028efffc140300010008fffca006fffc1483002f00040000040c00bc028e00a7030f00ff000413e000050000000413e100050000000413e200050000000000001781fffe1e8300001f03000018110000486b*"
data = "*0000cafeffff0384ffff0284031400040007030f00af00040006000e0000f806fffef40600001e81fffc1f88006100040068030f000b000e0000f806fffef40600001e81fff61f8810000004fffca00600010004fffaa0060031000e00000004fff8a006002a000efffa1483006a00040000041cfff8148300002007000000070000000800000083fffc140300000406fffc140300020008fffca006fff8140300010008fff8a006fff81483006900040000040c001a028efffa140300010008fffaa006fffa1483002f00040000040c0017028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800010004fffca006005f000e00000004fffaa0060058000efffc1403ffff0108fffc1483006a00040000041cfffa148300002007000000070000000800000083006a00040000081cfffa150300004007000000070000000800000406fffa140300010008fffaa006fffa1483006900040000040c0044028efffc140300010008fffca006fffc1483002f00040000040c0041028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc150300ff091600ff091613e00082000800040000049913e2018213e1000200002894006a010400004d1c0000080700000007000000080000040613e100020001000813e1000513e10082006a00040000040c0090038e0000000413e1000513e200020001000813e2000513e20082003000040000040c0090038e003a030f000e030f0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc140300ff001600ff001613e000050000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f8840000004fffca006fffc140300010084000004060000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800000004fffca00600d2000e00000004fffaa00600cb000efffc1483006a00040000041cfffa14830000200700000007000000080000008400000406fffa140300010008fffaa006fffa1483006900040000040c00bf028efffc140300010008fffca006fffc1483002f00040000040c00bc028e00a7030f000f000413e000050000000413e100050000000413e200050000000000001781fffe1e8300001f03000018110000495b*"
data = "*0000cafeffff0384ffff0284031400040007030f00af00040006000e0000f806fffef40600001e81fffc1f8800610004006c030f0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff61f8810000004fffca00600010004fffaa0060035000e00000004fff8a006002e000efffa1483006a00040000041cfff8148300002007000000070000000800000083fffc140300000406fffc140300020008fffca006fff8140300010008fff8a006fff81483006900040000040c001e028efffa140300010008fffaa006fffa1483002f00040000040c001b028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800010004fffca0060063000e00000004fffaa006005c000efffc1403ffff0108fffc1483006a00040000041cfffa148300002007000000070000000800000083006a00040000081cfffa150300004007000000070000000800000406fffa140300010008fffaa006fffa1483006900040000040c0048028efffc140300010008fffca006fffc1483002f00040000040c0045028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc150300ff091600ff091613e00082000800040000049913e2018213e1000200002894006a010400004d1c0000080700000007000000080000040613e100020001000813e1000513e10082006a00040000040c0094038e0000000413e1000513e200020001000813e2000513e20082003000040000040c0094038e003e030f0012030f0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc140300ff001600ff001613e000050000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f8840000004fffca006fffc140300010084000004060000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800000004fffca00600d6000e00000004fffaa00600cf000efffc1483006a00040000041cfffa14830000200700000007000000080000008400000406fffa140300010008fffaa006fffa1483006900040000040c00c3028efffc140300010008fffca006fffc1483002f00040000040c00c0028e00ab030f000f000413e000050000000413e100050000000413e200050000000000001781fffe1e8300001f03000018110000dc16*"
data = "*0000cafeffff0384ffff0284031400040007030f00af00040006000e0000f806fffef40600001e81fffc1f8800610004006c030f0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff61f8810000004fffca00600000004fffaa0060035000e00000004fff8a006002e000efffa1483006a00040000041cfff8148300002007000000070000000800000083fffc140300000406fffc140300020008fffca006fff8140300010008fff8a006fff81483006900040000040c001e028efffa140300010008fffaa006fffa1483002f00040000040c001b028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800010004fffca0060063000e00000004fffaa006005c000efffc1403ffff0108fffc1483006a00040000041cfffa148300002007000000070000000800000083006a00040000081cfffa150300004007000000070000000800000406fffa140300010008fffaa006fffa1483006900040000040c0048028efffc140300010008fffca006fffc1483002f00040000040c0045028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc150300ff091600ff091613e00082000800040000049913e2018213e1000200002894006a010400004d1c0000080700000007000000080000040613e100020001000813e1000513e10082006a00040000040c0094038e0000000413e1000513e200020001000813e2000513e20082003000040000040c0094038e003e030f0012030f0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc140300ff001600ff001613e000050000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f8840000004fffca006fffc140300010084000004060000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800000004fffca00600d6000e00000004fffaa00600cf000efffc1483006a00040000041cfffa14830000200700000007000000080000008400000406fffa140300010008fffaa006fffa1483006900040000040c00c3028efffc140300010008fffca006fffc1483002f00040000040c00c0028e00ab030f000f000413e000050000000413e100050000000413e200050000000000001781fffe1e8300001f03000018110000dc17*"
data = "*0000cafeffff0384ffff0284031400040007030f00af00040006000e0000f806fffef40600001e81fffc1f88006100040079030f006100040079030f006100040079030f0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff61f8810000004fffca00600000004fffaa006003c000e00000004fff8a0060035000efffa14830000040100020104000040190000200700000007fff8148300002007000000070000000800000083fffc140300000406fffc140300020008fffca006fff8140300010008fff8a006fff81483000900040000040c0022028efffa140300010008fffaa006fffa1483000900040000040c001f028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800010004fffca0060070000e00000004fffaa0060069000efffc1403ffff0088fffc15030000080100020184000060190000400700000007fffa1503000040070000000700000008000001030000040100020184000060190000200700000007fffa148300002007000000070000000800000806fffa140300010008fffaa006fffa1483000900040000040c004f028efffc140300010008fffca006fffc1483000900040000040c004c028e0000000000001781fffe1e8300001f03000018110000f806fffef406fffcf00600001e81fff81f88fffa1603ff00121600001014fffaa006fffa150300ff091600ff091600640082000800040000041900660082006501820000091400000401000202040000801900002007000000070000600700000007000000080000080600650002000100080065000500650082000a00040000040c00a5038e000000040065000500660002000100080066000500660082000a00040000040c00a5038e0045030f0016030f0000000000001781fffc1e03fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc140300ff001600ff0016006400050000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f8840000004fffca006fffc140300010084000004060000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800000004fffca00600eb000e00000004fffaa00600e4000efffc14830000040100020104000040190000200700000007fffa14830000200700000007000000080000008400000406fffa140300010008fffaa006fffa1483000900040000040c00d5028efffc140300010008fffca006fffc1483000900040000040c00d2028e00bd030f000f000400640005000000040065000500000004006600050000000000001781fffe1e8300001f030000181100005c18*"
data = "*0000cafeffff0384ffff0284031400040007030f00af00040006000e0000f806fffef40600001e81fffc1f8800cc030f00610004007a030f00610004007a030f00610004007a030f0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff61f8810000004fffca00600000004fffaa006003d000e00000004fff8a0060036000efffa14830000040100020104000040190000200700000007fff8148300002007000000070000000800000083fffc140300000406fffc140300020008fffca006fff8140300010008fff8a006fff81483000900040000040c0023028efffa140300010008fffaa006fffa1483000900040000040c0020028e0000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800010004fffca0060071000e00000004fffaa006006a000efffc1403ffff0088fffc15030000080100020184000060190000400700000007fffa1503000040070000000700000008000001030000040100020184000060190000200700000007fffa148300002007000000070000000800000806fffa140300010008fffaa006fffa1483000900040000040c0050028efffc140300010008fffca006fffc1483000900040000040c004d028e0000000000001781fffe1e8300001f03000018110000f806fffef406fffcf00600001e81fff81f88fffa1603ff00121600001014fffaa006fffa150300ff091600ff091600640082000800040000041900660082006501820000091400000401000202040000801900002007000000070000600700000007000000080000080600650002000100080065000500650082000a00040000040c00a6038e000000040065000500660002000100080066000500660082000a00040000040c00a6038e0046030f0017030f0000000000001781fffc1e03fffe1e8300001f03000018110000f806fffef40600001e81fffa1f88fffc1603ff00121600001014fffca006fffc140300ff001600ff0016006400050000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fffa1f8840000004fffca006fffc140300010084000004060000000000001781fffe1e8300001f03000018110000f806fffef40600001e81fff81f8800000004fffca00600ec000e00000004fffaa00600e5000efffc14830000040100020104000040190000200700000007fffa14830000200700000007000000080000008400000406fffa140300010008fffaa006fffa1483000900040000040c00d6028efffc140300010008fffca006fffc1483000900040000040c00d3028e00be030f000f000400640005000000040065000500000004006600050000000000001781fffe1e8300001f030000181100005829*"
if(len(sys.argv) > 1):
    f = open(sys.argv[1])
    data = f.read()
else:
    data = input("send: ") #ach.. this doesn't work when reading > 4095 chars! (see linux termios icannon)

it = 0
for c in data:
    ser.write(bytes([ord(c)]))
    it = it+1
    if(it%int(len(data)/100) == 0):
        print(int(it/int(len(data)/100)), end = " ", flush = True)
    sleep(0.002)
print()

ser.close()
