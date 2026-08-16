# # import pytest


# # def pytest_addoption(parser):

# #     parser.addoption(
# #         "--headless",
# #         action="store",
# #         default="true",
# #         help="Run browser headless or headed"
# #     )


# # @pytest.fixture(scope="function")
# # def page(playwright, request):

# #     headless_option = request.config.getoption("--headless")


# #     headless = headless_option.lower() == "true"


# #     browser = playwright.chromium.launch(
# #         headless=headless
# #     )


# #     page = browser.new_page()


# #     yield page


# #     browser.close()



# import pytest
# import os

# def pytest_addoption(parser):

#     parser.addoption(
#         "--headless",
#         action="store",
#         default="true",
#         help="Run browser headless or headed"
#     )


# @pytest.fixture(scope="function")
# def page(playwright, request):

#     headless_option = request.config.getoption("--headless")


#     headless = headless_option.lower() == "true"


#     browser = playwright.chromium.launch(
#         headless=headless,
#         args=["--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
#     )


#     page = browser.new_page()


#     yield page

#     os.makedirs("screenshots", exist_ok=True)
#     screenshot_path = f"screenshots/{request.node.name}.png"
#     page.screenshot(path=screenshot_path)


#     browser.close()

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == "call":
#         screenshot_path = f"screenshots/{item.name}.png"
#         if os.path.exists(screenshot_path):
#             import base64
#             with open(screenshot_path, "rb") as f:
#                 encoded = base64.b64encode(f.read()).decode()
#             html = f'<div><img src="data:image/png;base64,{encoded}" style="width:280px;" onclick="window.open(this.src)"/></div>'
#             if not hasattr(report, "extra"):
#                 report.extra = []
#             from pytest_html import extras
#             report.extra.append(extras.html(html))



# import os
# import base64
# import pytest
# from pytest_html import extras


# def pytest_addoption(parser):
#     parser.addoption(
#         "--headless",
#         action="store",
#         default="true",
#         help="Run browser headless or headed"
#     )


# @pytest.fixture(scope="function")
# def page(playwright, request):

#     headless_option = request.config.getoption("--headless")
#     headless = headless_option.lower() == "true"

#     browser = playwright.chromium.launch(
#         headless=headless,
#         args=["--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu","--disable-software-rasterizer","--window-size=1280,780"]
#     )

#     page = browser.new_page()

#     yield page

#     browser.close()


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()

#     if report.when == "call":
#         page = item.funcargs.get("page")
#         if page:
#             os.makedirs("screenshots", exist_ok=True)
#             screenshot_path = f"screenshots/{item.name}.png"
#             try:
#                 page.screenshot(path=screenshot_path, timeout=5000)
#                 with open(screenshot_path, "rb") as f:
#                     encoded = base64.b64encode(f.read()).decode()
#                 html = f'<div><img src="data:image/png;base64,{encoded}" style="width:280px;" onclick="window.open(this.src)"/></div>'
#                 if not hasattr(report, "extra"):
#                     report.extra = []
#                 report.extra.append(extras.html(html))
#             except Exception as e:
#                 print(f"Screenshot failed for {item.name}: {e}")










import os
import shutil
import pytest

from pytest_html import extras


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store",
        default="true",
        help="Run browser headless or headed"
    )


# @pytest.fixture(scope="function")
# def page(playwright, request):

#     headless = request.config.getoption("--headless").lower() == "true"

#     browser = playwright.chromium.launch(
#         headless=headless,
#         args=[
#             "--no-sandbox",
#             "--disable-dev-shm-usage",
#             "--disable-gpu"
#         ]
#     )

#     context = browser.new_context(
#         viewport={
#             "width": 1920,
#             "height": 1080
#         },
#         record_video_dir="videos",
#         record_video_size={
#             "width": 1920,
#             "height": 1080
#         }
#     )


#     context.tracing.start(
#         screenshots=True,
#         snapshots=True,
#         sources=True
#     )


#     page = context.new_page()


#     yield page


#     # Save video
#     video_path = None

#     if page.video:
#         video_path = page.video.path()


#     context.close()


#     # Rename video
#     if video_path and os.path.exists(video_path):

#         os.makedirs("videos", exist_ok=True)

#         new_video = f"videos/{request.node.name}.webm"

#         shutil.move(
#             video_path,
#             new_video
#         )


#     # Save trace only if failed
#     report = request.node.rep_call

#     if report.failed:

#         os.makedirs("traces", exist_ok=True)

#         context.tracing.stop(
#             path=f"traces/{request.node.name}.zip"
#         )

#     else:
#         context.tracing.stop()


#     browser.close()

@pytest.fixture(scope="function")
def page(playwright, request):

    headless = os.getenv("HEADLESS","true").lower()=="true"

    browser = playwright.chromium.launch(
        headless=headless,
        args=[
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu"
        ]
    )

    context = browser.new_context(
        viewport={
            "width": 1920,
            "height": 1080
        },
        record_video_dir="videos",
        record_video_size={
            "width": 1920,
            "height": 1080
        }
    )

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()

    yield page


    # Get test result safely
    report = getattr(request.node, "rep_call", None)


    # Stop tracing before closing context
    if report and report.failed:

        os.makedirs("traces", exist_ok=True)

        context.tracing.stop(
            path=f"traces/{request.node.name}.zip"
        )

    else:
        context.tracing.stop()


    # Save screenshot on failure
    if report and report.failed:

        os.makedirs("screenshots", exist_ok=True)

        page.screenshot(
            path=f"screenshots/{request.node.name}.png"
        )


    # Save video path before closing
    video_path = None

    if page.video:
        video_path = page.video.path()


    # Now close context
    context.close()


    # Move video after context closes
    if video_path and os.path.exists(video_path):

        os.makedirs("videos", exist_ok=True)

        shutil.move(
            video_path,
            f"videos/{request.node.name}.webm"
        )


    browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(
        item,
        "rep_" + report.when,
        report
    )


    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            os.makedirs(
                "screenshots",
                exist_ok=True
            )

            path = (
                f"screenshots/{item.name}.png"
            )

            page.screenshot(
                path=path
            )