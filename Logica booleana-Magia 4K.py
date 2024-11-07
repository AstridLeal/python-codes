# 24K=99,9%
# 22K=91,7%
# 20K=83.3%
# 18K=75.0%

purity=float(input())

if purity>=75.0 and purity<=83.3:
    print("18K")
elif purity>=83.3 and purity<=91.7:
    print("20K")
elif purity>=91.7 and purity<=99.9:
    print("22K")
elif purity>=99.9 and purity<=100.0:
    print("24K")