import pandas,sys

if len(sys.argv) != 3:
    print("Insufficient number of parameters.")

csvname = sys.argv[1]
clk_period = float(sys.argv[2])

df = pandas.read_csv(csvname)

def custom_round(x, base=5):
    return base * round(float(x)/base)

print(df.iloc[:,0])

df['difference'] = df.iloc[:,0].diff().fillna('0');
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

mean=0
for i in bitstream:
    mean+=i
mean = mean/len(bitstream)
print(f'mean is {mean}')
