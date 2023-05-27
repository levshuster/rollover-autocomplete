#Persistent

keysPressed := {}

SetTimer, CheckInput, 10
return

CheckInput:
Loop, 26 ; Loop through each letter of the alphabet
{
    key := Chr(A_Index + 64) ; Get the corresponding key (A=1, B=2, etc.)
    
    input := ""
    for index, tempkey in keysPressed
    {
        input .= tempkey
        ; input := tempkey
    }
    
    if GetKeyState(key, "P") ; Check if the key is currently pressed
    {
        keysPressed[key] := key
        ; MsgBox, Key added: %key%
    }
    else if keysPressed.HasKey(key)
    {
        if StrLen(input) > 2 {
            MsgBox, Keys pressed: %input%
            keysPressed := {}
        }
        else
        {
            keysPressed.Delete(key)
            ; MsgBox, Key deleted: %key%
        }
    }
}
return