@echo off
setlocal

:: Check if a file argument is provided
if "%~1"=="" (
    echo Error: Please provide a C file to compile
    echo Usage: %0 filename.c
    exit /b 1
)

:: Get the input file
set "input_file=%~1"

:: Check if the file exists
if not exist "%input_file%" (
    echo Error: File '%input_file%' not found
    exit /b 1
)

:: Compile the code
g++ -o out "%input_file%" -lfreeglut -lglew32 -lopengl32

:: Check if compilation was successful
if %ERRORLEVEL%==0 (
    echo Compilation successful
    :: Run the output
    out.exe
) else (
    echo Compilation failed
    exit /b 1
)

endlocal
