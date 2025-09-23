matrix = []
while True:
    line = input().strip()
    if line == "-1":
        break
    if not line:
        continue
    parts = line.split()
    if len(parts) < 4:
        continue
    name = parts[0]
    try:
        n1 = float(parts[1]); n2 = float(parts[2]); n3 = float(parts[3])
    except:
        continue
    matrix.append([name, f"{n1:.1f}", f"{n2:.1f}", f"{n3:.1f}"])

print("Matriz de notas:")
if matrix:
    print("[", end="")
    for i, row in enumerate(matrix):
        row_str = " ".join(f"'{x}'" for x in row)
        if i == 0:
            print(f"[{row_str}]", end="")
        else:
            print(f"\n [{row_str}]", end="")
    print("]")
else:
    print("[]")

max_media = None
nome_max = ""
for row in matrix:
    notas = [float(row[1]), float(row[2]), float(row[3])]
    media = sum(notas) / 3
    if (max_media is None) or (media > max_media):
        max_media = media
        nome_max = row[0]

if max_media is None:
    print("\nMaior média: 0.00 ()")
else:
    print(f"\nMaior média: {max_media:.2f} ({nome_max})")
