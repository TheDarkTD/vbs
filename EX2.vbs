Dim vetor(10)
Dim i, parCount, mult5Count, maiorNumero, menorNumero
Dim maiorIndice, menorIndice

For i = 0 To 9
    vetor(i) = InputBox("Digite o n�mero " & (i + 1) & ":")
Next

parCount = 0
mult5Count = 0
maiorNumero = CInt(vetor(0))
menorNumero = CInt(vetor(0))
maiorIndice = 0
menorIndice = 0
For i = 0 To 9
    If CInt(vetor(i)) Mod 2 = 0 Then
        parCount = parCount + 1
    End If
    If CInt(vetor(i)) Mod 5 = 0 Then
        mult5Count = mult5Count + 1
    End If
    If CInt(vetor(i)) > maiorNumero Then
        maiorNumero = CInt(vetor(i))
        maiorIndice = i
    End If
    If CInt(vetor(i)) < menorNumero Then
        menorNumero = CInt(vetor(i))
        menorIndice = i
    End If
Next
MsgBox "Quantidade de n�meros pares: " & parCount
MsgBox "Quantidade de n�meros m�ltiplos de 5: " & mult5Count
MsgBox "Maior n�mero: " & maiorNumero & " (�ndice: " & maiorIndice & ")"
MsgBox "Menor n�mero: " & menorNumero & " (�ndice: " & menorIndice & ")"
