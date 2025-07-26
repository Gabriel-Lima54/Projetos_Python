arq = open('dados.csv', 'w')
arq.write("Nome;Código;Quantidade;Preço;Categoria\n")
while (1):
  cod = int(input('\nDigite o código do produto: '))
  if (cod == -1):
    break
  nome = input('\nDigite o nome do produto: ')
  quant = int(input('\nDigite a quantidade do produto: '))
  preco = float(input('\nDigite o preço unitário do produto: '))
  cat = input('\nDigite a categoria do produto (A - Alimento, B - Bebida, H - Higiene, L - Limpeza, O - Outros): ')
  print('-'*20)
  arq.write(f'{cod};{nome};{quant};{preco};{cat}\n')
arq.close()

quant_total = 0
val_total = []

quant_a = 0
val_a = []

quant_b = 0
val_b = []

quant_h = 0
val_h = []

quant_l = 0
val_l = []

quant_o = 0
val_o = []

arq = open('dados.csv', 'r')
arq.readline()
for linha in arq:
  cod, nome, quant, preco, cat = linha.strip().split(';')
  print(f'\nCódigo = {cod}\nNome = {nome}\nQuantidade = {quant}\nPreço unitário = {preco}\nCategoria = {cat}\n')
  print('-'*20)
  if (cat == 'A'):
    quant_a += int(quant)
    val_a.append(int(quant) * float(preco))
    val_total.append(int(quant) * (float(preco)))
    quant_total += int(quant)
  elif (cat == 'B'):
    quant_b += int(quant)
    val_b.append(int(quant) * float(preco))
    val_total.append(int(quant) * (float(preco)))
    quant_total += int(quant)
  elif (cat == 'H'):
    quant_h += int(quant)
    val_h.append(int(quant) * float(preco))
    val_total.append(int(quant) * (float(preco)))
    quant_total += int(quant)
  elif (cat == 'L'):
    quant_l += int(quant)
    val_l.append(int(quant) * float(preco))
    val_total.append(int(quant) * (float(preco)))
    quant_total += int(quant)
  elif (cat == 'O'):
    quant_o += int(quant)
    val_o.append(int(quant) * float(preco))
    val_total.append(int(quant) * (float(preco)))
    quant_total += int(quant)
arq.close()



print(f"\nQuantidade total de itens no estoque: {quant_total}")
print(f"Valor total do estoque: R$ {sum(val_total)}\n")
print('-'*20)

print("\nCategorias")
print(f"\nAlimentos\nQuantidade: {quant_a}\nValor total: R${sum(val_a)}")
print(f"\nBebidas\nQuantidade: {quant_b}\nValor total: R${sum(val_b)}")
print(f"\nHigiene\nQuantidade: {quant_h}\nValor total: R${sum(val_h)}")
print(f"\nLimpeza\nQuantidade: {quant_l}\nValor total: R${sum(val_l)}")
print(f"\nOutros\nQuantidade: {quant_o}\nValor total: R${sum(val_o)}\n")
print('-'*20)

print("\nMédia dos preços:")
if ((quant_a) > 0):
  print(f"Alimentos: R$ {(sum(val_a) / quant_a):.2f}")
else:
  print(f"Alimentos: R$ 0")
if (quant_b > 0):
  print(f"Bebidas: R$ {(sum(val_b) / quant_b):.2f}")
else:
  print(f"Bebidas: R$ 0")
if (quant_h > 0):
  print(f"Higiene: R$ {(sum(val_h) / quant_h):.2f}")
else:
  print(f"Higiene: R$ 0")
if (quant_l > 0):
  print(f"Limpeza: R$ {(sum(val_l) / quant_l):.2f}")
else:
  print(f"Limpeza: R$ 0")
if (quant_o > 0):
  print(f"Outros: R$ {(sum(val_o) / quant_o):.2f}\n")
else:
  print(f"Outros: R$ 0\n")
print('-'*20)

print("\nPorcentagens")
print(f"\nAlimentos: {(sum(val_a) / sum(val_total)) * 100}%")
print(f"\nBebidas: {(sum(val_b) / sum(val_total)) * 100}%")
print(f"\nHigiene: {(sum(val_h) / sum(val_total)) * 100}%")
print(f"\nLimpeza: {(sum(val_l) / sum(val_total)) * 100}%")
print(f"\nOutros: {(sum(val_o) / sum(val_total)) * 100}%")