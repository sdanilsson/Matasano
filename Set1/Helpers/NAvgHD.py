'''
@Param blockList list of sublists

http://trustedsignal.blogspot.com/2015/06/xord-play-normalized-hamming-distance.html
HD = Hamming
Distance
AvgHD = HD / bytes
NAvgHD = AvgHD / Key Size

iterable cycle seems useful for creating the repeating key
'''
from __future__ import division

def getNormalizedHammingDistance(ks,blocklist):
    blocks = [blocklist[x:x + ks] for x in xrange(0, len(blocklist), ks)]

    hd = 0
    for i in range(len(blocks)):
        a = i % len(blocks) ; b = i % len(blocks) + 2
        tmp_lst = blocks[a: b]
        try:
            bl1 = ''.join(tmp_lst[0])
            bl2 = ''.join(tmp_lst[1])
            # print bl1,bl2
            hd = hd + sum(c1 != c2 for c1, c2 in zip(bl1, bl2))
        except IndexError:
            pass

    #print len(blocks)
    #print 'hd '+str(hd)
    avghd = hd / len(blocks)
    #print 'avghd: '+str(avghd)
    navghd = avghd / ks
    return navghd