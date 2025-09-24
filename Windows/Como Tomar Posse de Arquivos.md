# Como tomar posse de arquivos do Windows


'''
:: 1) Take ownership (recursively). Sets owner to your current user.
takeown /F "D:\OldData" /R /D Y

:: 2) Ensure inheritance is enabled on the root folder
icacls "D:\OldData" /inheritance:e

:: 3) Grant your account Full Control, recursively (OI/CI apply to files/folders)
icacls "D:\OldData" /grant:r "%USERNAME%":(OI)(CI)F /T /C /Q
'''