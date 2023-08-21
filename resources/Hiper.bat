@echo off
color 0c
pushd %~dp0
cls
openfiles > NUL 2>&1
if %errorlevel%==0 (
	echo 	Privil‚gios de Administrador Encontrados! Continuando...
	cls
	goto :go
) else (
	echo   Por Favor Execute esse Programa como Administrador.
	echo.
	echo  				~ Pressione qualquer tecla para sair... ~
	pause > NUL
	exit
)

:go
color 07
echo.
:::     _    _   _____   _____    ______   _____
:::    | |  | | |_   _| |  __ \  |  ____| |  __ \
:::    | |__| |   | |   | |__) | | |__    | |__) |
:::    |  __  |   | |   |  ___/  |  __|   |  _  /
:::    | |  | |  _| |_  | |      | |____  | | \ \
:::    |_|  |_| |_____| |_|      |______| |_|  \_\
for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A
echo                                  Pre-Implantacao
SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%b in ('"prompt #$H#$E# & echo on & for %%b in (1) do     rem"') do (
  set "DEL=%%b"
)
for /f "tokens=4-5 delims=. " %%i in ('ver') do set VERSION=%%i.%%j
if "%version%" == "10.0" (
SET "winvers=Windows 10"
)
if "%version%" == "6.3"  (
SET "winvers=Windows 8.1"
)
if "%version%" == "6.2" (
SET "winvers=Windows 8"
)
if "%version%" == "6.1" (
SET "winvers=Windows 7"
)
if "%version%" == "6.0" (
SET "winvers=Windows Vista"
)
reg query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" > NUL && set OS=32 || set OS=64
echo.
call :colorEcho 0a "     %winvers% x%OS%bits"
echo.
echo.
echo      #######################################
echo.
echo.
if %OS%==32 (
call :colorEcho 0a "     Iniciando o Download do SQL Server 2014... "
start https://download.microsoft.com/download/E/A/E/EAE6F7FC-767A-4038-A954-49B8B05D04EB/Express%%2032BIT/SQLEXPR_x86_ENU.exe
echo.
echo.
call :colorEcho 0a "     Iniciando o Download do SQL Management Studio 2014... "
start https://download.microsoft.com/download/0/1/5/015567C0-E851-4AC6-964F-9BBA9B31D6BC/MgmtStudio%%2032BIT/SQLManagementStudio_x86_PTB.exe
echo.
echo.
call :colorEcho 0a "     Iniciando o Download do Setup do Hiper... "
start https://downloads.hiper.com.br/Hiper.Setup.exe
)
if %OS%==64 (
call :colorEcho 0a "     Iniciando o Download do SQL Server 2014... "
start https://download.microsoft.com/download/E/A/E/EAE6F7FC-767A-4038-A954-49B8B05D04EB/Express%%2064BIT/SQLEXPR_x64_ENU.exe
echo.
echo.
call :colorEcho 0a "     Iniciando o Download do SQL Management Studio 2014... "
start https://download.microsoft.com/download/0/1/5/015567C0-E851-4AC6-964F-9BBA9B31D6BC/MgmtStudio%%2064BIT/SQLManagementStudio_x64_PTB.exe
echo.
echo.
call :colorEcho 0a "     Iniciando o Download do Setup do Hiper... "
start https://downloads.hiper.com.br/Hiper.Setup.exe
)
echo.
echo.
echo      #######################################
netsh int ipv6 set teredo disabled > NUL
netsh int ipv6 isatap set state disabled > NUL
netsh int ipv6 6to4 set state disabled > NUL
echo.
call :colorEcho 0a "     [OK] Protocolo TCP - IPv6 Desabilitado!"
echo.
echo.
echo      #######################################
echo.
if "%winvers%" == "Windows 8" (
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v SecureProtocols /t REG_DWORD /d 00002720 /f >NUL
call :colorEcho 0a "     [OK] TLS 1.1 e 1.2 do Windows Ativados!"
)
if "%winvers%" == "Windows 8.1" (
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v SecureProtocols /t REG_DWORD /d 00002720 /f >NUL
call :colorEcho 0a "     [OK] TLS 1.1 e 1.2 do Windows Ativados!"
)
if "%winvers%" == "Windows 10" (
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v SecureProtocols /t REG_DWORD /d 00002720 /f >NUL
call :colorEcho 0a "     [OK] TLS 1.1 e 1.2 do Windows Ativados!"
)
if "%winvers%" == "Windows 7" (
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Client" /v DisabledByDefault /t REG_DWORD /d 00000000 /f >NUL
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server" /v DisabledByDefault /t REG_DWORD /d 00000000 /f >NUL
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client" /v DisabledByDefault /t REG_DWORD /d 00000000 /f >NUL
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server" /v DisabledByDefault /t REG_DWORD /d 00000000 /f >NUL
call :colorEcho 0a "     [OK] TLS 1.1 e 1.2 do Windows Ativados!"
)
echo.
echo.
echo      #######################################
echo.
call :colorEcho 0a "     [-] Iniciando Recursos do Windows..."
optionalfeatures > NUL
echo.
echo.
echo      #######################################
echo.
pause > NUL
:colorEcho
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1i