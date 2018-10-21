'Author: Simon Ross
'Language: VBScript
'Github: https://github.com/skar4242

For n = 1 To 100
	strThree = n Mod 3
	strFive = n Mod 5
	Do Until simon = 42
		If strThree = 0 And strFive = 0 Then
			WScript.Echo "SPIDERS(" & n & ")"
			Exit do
		ElseIf strThree = 0 Then
			WScript.Echo "CATS(" & n & ")"
			Exit do
		ElseIf strFive = 0 Then
			WScript.Echo "BATS(" & n & ")"
			Exit do
		Else
			WScript.Echo n
			Exit do
		End If
	Loop
Next