import pandas,sys

if len(sys.argv) != 3:
    print("Insufficient number of parameters.")

csvname = sys.argv[1]
clk_period = float(sys.argv[2])

df = pandas.read_csv(csvname)

def custom_round(x, base=5):
    return base * round(float(x)/base)

df['difference'] = df['a2d_OUT X'].diff().fillna('0');
df['diffrounded'] = df['difference'].apply(lambda x: custom_round(x, base=float(clk_period)))
df['numclks'] = (df['diffrounded']/clk_period).apply(lambda x: int(x))

bitstream=[]

for i, numclks in enumerate(df['numclks']):
    if i%2==0:
        for j in range(numclks):
            bitstream.append(1)
    else:
        for j in range(numclks):
            bitstream.append(0)

bithalf1 = bitstream[:len(bitstream)//2]
bithalf2 = bitstream[len(bitstream)//2:]

del bithalf1[len(bithalf2):]
del bithalf2[len(bithalf1):]

bitq1 = bithalf1[len(bithalf1)//2:]
bitq2 = bithalf1[:len(bithalf1)//2]
bitq3 = bithalf2[len(bithalf2)//2:]
bitq4 = bithalf2[:len(bithalf2)//2]

bito1 = bitq1[len(bitq1)//2:]
bito2 = bitq1[:len(bitq1)//2]
bito3 = bitq2[len(bitq2)//2:]
bito4 = bitq2[:len(bitq2)//2]
bito5 = bitq3[len(bitq3)//2:]
bito6 = bitq3[:len(bitq3)//2]
bito7 = bitq4[len(bitq4)//2:]
bito8 = bitq4[:len(bitq4)//2]

outstring=""

for i, val in enumerate(bito1):
    if ((bito1[i] != bito2[i]) != (bito3[i] != bito4[i])) != ((bito5[i] != bito6[i]) != (bito7[i] != bito8[i])):
        outstring += '1';
    else:
        outstring += '0';

print(outstring)
