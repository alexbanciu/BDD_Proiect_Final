from browser import Browser


class TitlePage(Browser):

    def is_page_title_displayed(self):
        return "Amazon" in self.chrome.title