from playwright.sync_api import sync_playwright, expect, Page
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def test_static_web_Table(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #locating table
    table=page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()

    #1. count total number of rows in a table
    rows=table.locator("tr")   # equals to table[name='BookTable'] tbody tr
    expect(rows).to_have_count(7)

    row_count=rows.count()
    print("Number of rows in a table:",row_count )  # 7

    # 2. count total number of columns/headers in table
    columns=rows.locator("th")  # equals to table[name='BookTable'] tbody tr th
    expect(columns).to_have_count(4)

    column_count=columns.count()
    print("Number of columns/headers in a table:", column_count)  #4

    #3. Read all the data from 2nd row of the table
    second_row_cells=rows.nth(2).locator('td')     # nth() index starts from 0
    second_row_texts=second_row_cells.all_inner_texts()
    print("2nd row data=====>:",second_row_texts) #['Learn Java', 'Mukesh', 'Java', '500']

    expect(second_row_cells).to_have_text(['Learn Java', 'Mukesh', 'Java', '500'])

    # print("Printing 2nd row data.......")
    logger.info("Printing 2nd row data.......")
    for text in second_row_texts:
        print(text)

    #4. Read all the data from the table ( Excluding header)
    all_row_data=rows.all()

    print("Printing data from all the rows and columns.......")
    # when we do [1:] we are using slice and specifying index as 1 to ignore header row
    for row in all_row_data[1:]:
        cols=row.locator('td').all_inner_texts()
        print(cols)

    # 5. Print Book names whose author is 'Mukesh'
    print("Printing Books names written By Mukesh........")
    for row in all_row_data[1:]:
        author_name=row.locator('td').nth(1).inner_text()
        if author_name=='Mukesh':
            book_name=row.locator('td').nth(0).inner_text()
            print(f"{author_name} \t {book_name}")

    #6. Calculate total price of all the books
    total_price=0
    for row in all_row_data[1:]:
        price=row.locator('td').nth(3).inner_text()
        total_price+=int(price)  #total_price=total_price+int(price)
    print("Total price:" , total_price)  # 7100


# Print all subjects
def test_print_all_subjects(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    all_rows_data = page.locator("table[name$='BookTable'] tbody tr").all()
    for row in all_rows_data[1:]:
        subject_name = row.locator("td").nth(2).inner_text().strip()
        print(subject_name)
















