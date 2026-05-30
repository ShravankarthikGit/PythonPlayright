import pytest
import re
from playwright.sync_api import Page, expect



def test_dynamic_table_chrome(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator("table#taskTable tbody tr").all()
    rowcount = len(rows)
    print (f"Row count in table: {rowcount}")
    cpu_load = ''
    for row in rows:
        process_name = row.locator("td").nth(0).inner_text()
        print (f"Process name: {process_name}")
        if process_name == "Chrome":
            cpu_load = row.locator("td", has_text="%").inner_text()
            print(f"Cpu load: {cpu_load}")
            break

    expect(page.locator("strong.chrome-cpu")).to_contain_text(cpu_load)


def test_dynamic_table_firefox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator("table#taskTable tbody tr").all()
    rowcount = len(rows)
    print (f"Row count in table: {rowcount}")
    memory = ''
    for row in rows:
        process_name = row.locator("td").nth(0).inner_text()
        print (f"Process name: {process_name}")
        if process_name == "Firefox":
            memory = row.locator("td").filter(has_text=re.compile(r"MB$")).inner_text().strip()
            print(f"Memory is : {memory}")
            break

    expect(page.locator("strong.firefox-memory")).to_contain_text(memory)


def test_dynamic_table_network_speed_chrome(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator("table#taskTable tbody tr").all()
    rowcount = len(rows)
    print(f"Row count in table: {rowcount}")
    network_speed = ''
    for row in rows:
        process_name = row.locator("td").nth(0).inner_text()
        print(f"Process name: {process_name}")
        if process_name == "Chrome":
            network_speed = row.locator("td").filter(has_text=re.compile(r"Mbps$")).inner_text().strip()
            # memory = row.locator("td").filter(has_text="MB").inner_text().strip()
            print(f"network_speed is : {network_speed}")
            break

    expect(page.locator("strong.chrome-network")).to_contain_text(network_speed)

def test_dynamic_table_disk_space_firefox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator("table#taskTable tbody tr").all()
    rowcount = len(rows)
    print (f"Row count in table: {rowcount}")
    disk_space = ''
    for row in rows:
        process_name = row.locator("td").nth(0).inner_text()
        print (f"Process name: {process_name}")
        if process_name == "Firefox":
            disk_space = row.locator("td").filter(has_text=re.compile(r"MB/s$")).inner_text().strip()
            print(f"disk_space is : {disk_space}")
            break

    expect(page.locator("strong.firefox-disk")).to_contain_text(disk_space)


# def test_paginated_table(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/")
#
#     pages = page.locator("ul[class='pagination'] li").all()
#     for pa in pages:
#         pa.click()
#         table_locator = page.locator("table[id='productTable'] tbody")
#         rows = table_locator.locator('tr').all()
#         for row in rows:
#             print(row.all_text_contents())












