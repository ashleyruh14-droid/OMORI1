Set fso = CreateObject("Scripting.FileSystemObject")
Set WshShell = CreateObject("WScript.Shell")

' Dossier où se trouve ce .vbs
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)

' Chemin complet vers le .bat
batPath = """" & scriptDir & "\lancer.bat" & """"

' 0 = masqué, False = ne pas attendre la fin du .bat
WshShell.Run batPath, 0, False

Set WshShell = Nothing
Set fso = Nothing
