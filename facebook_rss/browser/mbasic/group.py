# pylint: disable=R0801
from playwright.async_api import Page

from facebook_rss.browser.mbasic.profile import ProfilePage


class GroupPage(ProfilePage):

    def __init__(self, page: Page, group: str):
        super().__init__(page, group)
        self.account = group
        self._is_group = True

    @classmethod
    async def create(cls, page: Page, profile: str):
        self = GroupPage(page, profile)
        current_url = await self.get_actual_url()
        if current_url != self.url:
            await self.open(self.url)
        return self

    @property
    def posts_selector(self):
        # return '//article[contains(@data-ft,"top_level_post_id")]//p'
        return '//a[contains(@href, "/permalink/") and contains(text(), "Full Story")]'

    @property
    async def is_private(self):
        return bool(await self.page.query_selector(
            '//a[contains(@href, "/login/") and contains(text(), "Join Group")]'))

    @property
    def url(self) -> str:
        return f"https://mbasic.facebook.com/groups/{self.account}/"

    @property
    def _author_selector(self):
        return "//strong/a"

    @property
    def _attached_link_selector(self):
        return "a.eg.ec"

    @property
    def _image_selector(self):
        return "img.t"

    @property
    def _video_selector(self):
        return "//a[starts-with(@href, '/video_redirect/')]"
