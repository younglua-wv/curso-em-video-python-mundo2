seg_a = float(input("Qual o valor do primeiro segmento? "))
seg_b = float(input("Qual o valor do segundo segmento? "))
seg_c = float(input("Qual o valor do terceiro segmento? "))

if seg_a + seg_b > seg_c and seg_b + seg_c > seg_a and seg_a + seg_c > seg_b:
  print("Os segmentos acima PODEM FORMAR um triângulo ", end="")
  if seg_a == seg_b == seg_c:
    print("EQUILÁTERO!")
  elif seg_a != seg_b != seg_c:
    print("ESCALENO!")
  else:
    print("ISÓSCELES!")
else:
  print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")