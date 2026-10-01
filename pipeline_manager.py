"""
Pipeline Manager for Autonomous Thesis Proposal Generation
Coordinates memory state, topic selection, and stage status.
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
MEMORY_DIR = BASE_DIR / "memory"
RULES_DIR = BASE_DIR / ".agents" / "rules"
OUTPUTS_DIR = BASE_DIR / "outputs"


def load_json(filepath: Path) -> dict:
    if not filepath.exists():
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(filepath: Path, data: dict):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_status():
    state = load_json(MEMORY_DIR / "state_tracker.json")
    active = load_json(MEMORY_DIR / "active_project.json")
    
    print("=" * 60)
    print("  TEZ HAZIRLAMA OTONOM PIPELINE DURUMU")
    print("=" * 60)
    print(f"Mevcut Aşama: {state.get('current_stage', 0)} - {state.get('stage_name', 'Bilinmiyor')}")
    print(f"Aktif Konu ID: {active.get('topic_id', 'Seçilmedi')}")
    if active.get('selected_topic'):
        print(f"Konu Başlığı: {active['selected_topic']}")
    print("-" * 60)
    print("Aşama İlerlemeleri:")
    for key, stage in state.get("stages", {}).items():
        status = "[TAMAMLANDI]" if stage.get("completed") else "[BEKLİYOR]"
        print(f"  * {stage.get('name')}: {status}")
        if stage.get("details"):
            print(f"    -> {stage.get('details')}")
    print("=" * 60)


def list_topics():
    topics_data = load_json(MEMORY_DIR / "candidate_topics.json")
    print("=" * 70)
    print("  ADAY TEZ KONULARI (AI Studio Verisi)")
    print("=" * 70)
    for t in topics_data.get("topics", []):
        print(f"\n[{t['id']}] {t['short_name']} ({t['category']})")
        print(f"Başlık : {t['title']}")
        print(f"Yük    : {t['in_class_load']}")
        print(f"Analiz : {t['technical_analysis']}")
    print("=" * 70)


def select_topic(topic_id: str):
    topics_data = load_json(MEMORY_DIR / "candidate_topics.json")
    found = None
    for t in topics_data.get("topics", []):
        if t["id"].upper() == topic_id.upper():
            found = t
            break
            
    if not found:
        print(f"Hata: '{topic_id}' kodlu konu bulunamadı. Lütfen geçerli bir konu kodu girin.")
        return False
        
    active = load_json(MEMORY_DIR / "active_project.json")
    active["topic_id"] = found["id"]
    active["selected_topic"] = found["title"]
    active["category"] = found["category"]
    active["short_name"] = found["short_name"]
    active["status"] = "TOPIC_SELECTED"
    save_json(MEMORY_DIR / "active_project.json", active)
    
    state = load_json(MEMORY_DIR / "state_tracker.json")
    state["active_topic_id"] = found["id"]
    state["current_stage"] = 1
    state["stage_name"] = "STAGE_1_IN_PROGRESS"
    state["stages"]["stage_1"]["details"] = f"Seçilen konu: [{found['id']}] {found['short_name']}"
    save_json(MEMORY_DIR / "state_tracker.json", state)
    
    print(f"\n[BASARILI] Konu seçildi: [{found['id']}] {found['short_name']}")
    print(f"Başlık: {found['title']}")
    print("Aşama 1 (Tema, Araştırma Soruları ve Arama Sorguları) hazırlandı.")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        get_status()
    elif sys.argv[1] == "status":
        get_status()
    elif sys.argv[1] == "list-topics":
        list_topics()
    elif sys.argv[1] == "select-topic" and len(sys.argv) > 2:
        select_topic(sys.argv[2])
    else:
        print("Kullanım: python pipeline_manager.py [status | list-topics | select-topic <ID>]")
