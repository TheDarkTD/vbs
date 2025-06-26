Randomize

Dim min, max, qtd, i
Dim dict, chave, valor

Set dict = CreateObject("Scripting.Dictionary")

min = InputBox("Digite o valor mínimo da faixa:")
max = InputBox("Digite o valor máximo da faixa:")
qtd = InputBox("Digite a quantidade de números a sortear:")

For i = 1 To qtd
    valor = Int((max - min + 1) * Rnd + min)
    chave = "Sorteio " & i
    dict.Add chave, valor
Next

Dim resultado
resultado = "Números sorteados com chaves:" & vbCrLf

For Each chave In dict.Keys
    resultado = resultado & chave & ": " & dict(chave) & vbCrLf
Next

MsgBox resultado
