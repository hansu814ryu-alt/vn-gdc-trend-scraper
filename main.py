from scrapers.facebook_scraper import FacebookGroupScraper
from scrapers.itviec_scraper import ITViecReviewScraper
from scrapers.threads_scraper import ThreadsKeywordScraper

def run_pipeline():
    print("==================================================")
    print(" Start Pipeline: Vietnam IT GDC Trend Collection  ")
    print("==================================================")

    # 파이프라인 인스턴스 등록
    pipeline_tasks = [
        FacebookGroupScraper(target_group_name="J2TEAM Community", cookie_path="secrets/fb_cookies.json"),
        ITViecReviewScraper(target_company_url="https://itviec.com/companies/sample-gdc"),
        ThreadsKeywordScraper(search_keyword="GDC Vietnam")
    ]

    # 공통 인터페이스 순회 구동
    for task in pipeline_tasks:
        try:
            task.collect_raw_data()
            task.save_to_json()
        except Exception as e:
            print(f"❌ Error in [{task.platform}]: {str(e)}")
        print("-" * 50)

if __name__ == "__main__":
    run_pipeline()
