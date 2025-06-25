Randomize

Dim min, max, qtd, i
Dim sorteios()

min = InputBox("Digite o valor mínimo da faixa:")
max = InputBox("Digite o valor máximo da faixa:")
qtd = InputBox("Digite a quantidade de números a sortear:")

ReDim sorteios(qtd - 1)

For i = 0 To qtd - 1
    sorteios(i) = Int((max - min + 1) * Rnd + min)
Next

Dim resultado
resultado = "Números sorteados:" & vbCrLf

For i = 0 To qtd - 1
    resultado = resultado & sorteios(i) & vbCrLf
Next

MsgBox resultado
