# Bonus task

paikka = "Patvinsuo"
pituus = 10.7
nopeus = 5.2

mailitperkm = 0.6214

place = "The" + " " + paikka
length = pituus * mailitperkm
speed = nopeus * mailitperkm

print(f"Place: {place}")
print(f"Length (miles): {length:.2f}")
print(f"Speed (mph): {speed:.3f}")