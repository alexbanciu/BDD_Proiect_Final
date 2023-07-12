from browser import Browser


class TitlePage(Browser):

    def is_page_title_displayed(self, title_page):
        assert f"{title_page}" in self.chrome.title, "Page title is not displayed correctly"
        return True