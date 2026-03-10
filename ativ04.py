nota=input("digite a nota do aluno(a):")
nota=float(nota)
notaalta=nota>=6.0
notabaixa=nota<6.0

if notaalta:
    print(f"A nota do aluno é:{nota}, aluno aprovado.")

else:
    print(f"A nota do aluno é:{nota}, aluno reprovado.")
