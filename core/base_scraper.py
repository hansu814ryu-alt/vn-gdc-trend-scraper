import os
import json
import random
import time
from abc import ABC, abstractmethod

class BaseScraper(ABC):
    """
    [부모 클래스] 모든 플랫폼별 스크래퍼의 기반 인터페이스 및 공통 전처리 레이어
    """
    def __init__(self, platform_name: str, target_source: str):
        self.platform = platform_name
        self.target_source = target_source
        self.output_data = []

    @abstractmethod
    def collect_raw_data(self):
        """자식 스크래퍼들이 개별적으로 알맹이를 채워야 하는 수집 추상 메서드"""
        pass

    def vietnamese_text_preprocessing(self, raw_text: str) -> str:
        """베트남어 텍스트 기본 정제 및 공백 처리 (공통 엔진)"""
        if not raw_text:
            return ""
        return raw_text.strip().replace("\n", " ")

    def apply_human_delay(self, min_sec=2.5, max_sec=6.2):
        """클라우드 환경 봇 차단 회피용 랜덤 지연 유틸리티"""
        time.sleep(random.uniform(min_sec, max_sec))

    def standardize_format(self, post_id: str, author: str, content: str, timestamp: str) -> dict:
        """sLLM 연동 규격에 맞춘 데이터 표준 정형 포맷화"""
        return {
            "platform": self.platform,
            "target_source": self.target_source,
            "post_id": post_id,
            "author_hash": hash(author), # 비식별화
            "raw_content": content,
            "refined_content": self.vietnamese_text_preprocessing(content),
            "collected_at": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
            "created_at": timestamp
        }

    def save_to_json(self, base_path="output/"):
        """정제 완료 데이터 JSON 파일 출력"""
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        filename = f"{base_path}{self.platform.lower()}_{time.strftime('%Y%m%d')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.output_data, f, ensure_ascii=False, indent=4)
        print(f" Saved: [{self.platform}] {len(self.output_data)} items -> {filename}")
