# autotest_landing_2.0_ExLab
UI automated tests for Exlab Start Up
git clone https://github.com/kolik1983/autotest_landing_2.0_ExLab.git
pip install -r requirements.txt
pytest -v -s  --tb=line --reruns 0  --browser_name=chrome --width_window=1920 --height_window=1080 --language=ru --headless=None --alluredir results tests/landing_tests.py
allure serve report/
