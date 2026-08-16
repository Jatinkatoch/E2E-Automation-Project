
@echo off

echo Running Playwright tests in HEADED mode...

@REM start "" http://localhost:6080/vnc.html

podman run --rm ^
--network ecommerce-network ^
-p 6080:6080 ^
-p 5900:5900 ^
-e HEADLESS=false ^
-v "%cd%\videos:/automation/videos" ^
-v "%cd%\reports:/automation/reports" ^
-v "%cd%\traces:/automation/traces" ^
-v "%cd%\screenshots:/automation/screenshots" ^
ecommerce-tests