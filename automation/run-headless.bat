@echo off

echo Running Playwright tests in HEADLESS mode...

podman run --rm ^
--network ecommerce-network ^
-v "%cd%\videos:/automation/videos" ^
-v "%cd%\reports:/automation/reports" ^
-v "%cd%\traces:/automation/traces" ^
-v "%cd%\screenshots:/automation/screenshots" ^
ecommerce-tests