kg = float ( input ( "Informe a quantidade de ração do saco em Kg: ") )
pesosaco = kg * 1000
gato1 = float ( input ( "Informe a quantidade de ração que o gato 1 consome diariamente: " ) )
gato2 = float ( input ( "Informe a quantidade de ração que o gato 2 consome diariamente: " ) )
tot5d = pesosaco - ( gato1 * 5 + gato2 * 5 )
print ( f"A quantidade restamte após 5 dias é { round ( tot5d,2 ) } " )