import pytest
import re
from playwright.sync_api import sync_playwright, expect,Page


def test_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames=page.frames
    print("Number of frames on a page:", len(frames))  # 3

    for frame in frames:
        print(frame)

    #<Frame name= url='https://ui.vision/demo/webtest/frames/'>
    #<Frame name= url='https://www.youtube.com/embed/yzVc13QdGxw?rel=0&cc_load_policy=1'>
    #<Frame name= url='https://forum.ocr.space//embed/topics?discourse_embed_id=de-54whb6zll&allow_create=true&template=complete&per_page=3'>

    # Matches the static parts of your URL, completely ignoring the dynamic session ID
    frame1 = page.frame(url=re.compile(r"https://forum\.ocr\.space//embed/topics"))
    page.wait_for_timeout(5000)

    if frame1 is not None:
        input_box = frame1.locator(".new-topic-btn__text")
        input_box.click()
        print("clicked")
    else:
        print("Frame was not found!")

    page.wait_for_timeout(5000)
