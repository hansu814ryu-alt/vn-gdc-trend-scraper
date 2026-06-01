from core.base_scraper import BaseScraper

class ITViecReviewScraper(BaseScraper):
    def __init__(self, target_company_url: str):
        super().__init__(platform_name="ITviec", target_source=target_company_url)

    def collect_raw_data(self):
        # ----------------------------------------------------
        # TODO: [B 개발자 담당 알맹이 영역]
        # BeautifulSoup를 사용해 해당 기업 리뷰 텍스트를 파싱하여
        # 부모의 구조 양식에 맞추어 self.output_data에 적재
        # ----------------------------------------------------
        pass
