Dim vetorA, vetorB, i, j, comuns
vetorA = Array(1, 3, 5, 7, 9)
vetorB = Array(2, 3, 5, 6, 7, 8, 9, 10)
comuns = ""


For i = 0 To UBound(vetorA)
    For j = 0 To UBound(vetorB)
        If vetorA(i) = vetorB(j) Then
            If InStr(comuns, CStr(vetorA(i)) & ",") = 0 Then
                comuns = comuns & vetorA(i) & ","
            End If
        End If
    Next
Next
If Right(comuns, 1) = "," Then
    comuns = Left(comuns, Len(comuns) - 1)
End If

MsgBox "Comuns entre os vetores: " & comuns