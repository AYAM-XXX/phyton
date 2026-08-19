n1, n2 = map(int, input().split(" "))
maior = n1 > n2
menor = n1 < n2
igual = n1  == n2
diferente = n1  != n2
maior_igual = n1 >= n2
menor_igual = n1 <= n2

print(f"o numero {n1} é  maior que  o numero {n2}: {maior}")
print(f"o numero {n1} é  menor que o  numero {n2}: {menor}")
print(f"o numero {n1} é igual o numero {n2}: {igual}")
print(f"o numero {n1} é diferente numero {n2}: {diferente}")
print(f"o numero {n1} é  maior igual que o numero {n2}: {maior_igual}")
print(f"o numero {n1} é  menor igual que o numero {n2}: {menor_igual}")

soma, sub, mult, div = map(int, input().split(" "))
soma += 2
sub -= 2
mult *= 2
div /= 2

print(f"{soma}\n{sub}\n{mult}\n{div}")
