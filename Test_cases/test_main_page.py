def test_for_choose_checkbox_wordfile(page):
    page.push_elemets_button()
    page.open_checkbox_page()
    page.push_toggle_home()
    page.push_toggle_downloads()
    page.choose_checkbox_wordfile()
