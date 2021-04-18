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

outstring = "";
for i, val in enumerate(bithalf1):
    if bithalf1[i] != bithalf2[i]:
        outstring += "1";
    else:
        outstring += "0";

print(outstring)
