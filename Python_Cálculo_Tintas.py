a_vf = int(input('Qual a área total a ser cultivada de Vinho fino?: '))
temp = input('Sera necessário reaplicar? use s ou n: ')
if temp == 's':
  adubo_vf = 4000
elif temp == 'n':
  adubo_vf = 1000
a_vc = int(input('\nQual a área total a ser cultivada de Vinho comum?: '))
adubo_vc = 2500
a_suco = int(input('\nQual a área total a ser cultivada de suco?: '))
adubo_suco = 1800

total_vf = (a_vf / adubo_vf)
total_vc = (a_vc / adubo_vc)
total_suco = (a_suco / adubo_suco)

arredondamento = int(total_vf)
if total_vf != arredondamento:
  total_vf = arredondamento + 1
else:
  total_vf = arredondamento

arredondamento = int(total_vc)
if total_vc != arredondamento:
  total_vc = arredondamento + 1
else:
  total_vc = arredondamento

arredondamento = int(total_suco)
if total_suco != arredondamento:
  total_suco = arredondamento + 1
else:
  total_suco = arredondamento

total_adubo = (total_suco + total_vc + total_vf)

print(f'\nÁreas de cultivo de:\nvinhos finos: {a_vf} m2\nvinhos comum: {a_vc} m2\nsucos: {a_suco} m2')
print(f'\nTotal de adubo necessario para cada cultivo:\nVinho fino = {total_vf}t\nVinho comum = {total_vc}t\nSucos = {total_suco}t')
print(f'\nTotal area de cultivo: {(a_vf + a_vc + a_suco)} m2')
print(f'Total de adubo para cobrir toda a area de cultivo: {total_adubo}t')

carga_1t = 0
carga_5t = 0
carga_12t = 0
sobra = 0

if total_adubo >= 12:
  carga_12t = total_adubo // 12
  sobra = total_adubo % 12
elif total_adubo >= 5:
  carga_5t = total_adubo // 5
  sobra = total_adubo % 5
else:
  carga_1t = total_adubo

if sobra >= 5:
  carga_5t = sobra // 5
  sobra = sobra % 5
if sobra >= 1:
  carga_1t = sobra // 1
  if sobra != int(sobra):
    carga_1t = 1

print(f'\nQuantidade de cargas de 1t = {carga_1t}')
print(f'\nQuantidade de cargas de 5t = {carga_5t}')
print(f'\nQuantidade de cargas de 12t = {carga_12t}')

valor_1t = 1200 * carga_1t
valor_5t = 5500 * carga_5t
valor_12t = 9600.00 * carga_12t

print('\npreço das cargas:\n1 tonelada, custo de R$ 1200.00\n5 toneladas, custo de R$ 5500.00\n12 toneladas, custo de R$ 9600.00')
print(f'\nCusto total das viagens = R$ {(valor_1t + valor_5t + valor_12t):.2f}')