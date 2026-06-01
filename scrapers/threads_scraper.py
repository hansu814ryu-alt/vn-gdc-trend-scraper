from core.base_scraper import BaseScraper

class ThreadsKeywordScraper(BaseScraper):
    def __init__(self, search_keyword: str):
        super().__init__(platform_name="Threads", target_source=search_keyword)

    def collect_raw_data(self):
        # ----------------------------------------------------
        # TODO: [C 개발자 담당 알맹이 영역]
        # Apify Actor API 혹은 사설 API 호스트 엔드포인트를 호출하여
        # 키워드 검색 결과 텍스트 데이터를 받아 정형화 처리
        # ----------------------------------------------------
        pass
