
import unittest
import os

class TestProjectStructure(unittest.TestCase):
    
    def test_notebooks_exist(self):

        notebooks = [
            "notebooks/01_data_preparation.ipynb",
            "notebooks/02_baseline_model.ipynb",
            "notebooks/03_model_experiment.ipynb",  # БЕЗ 's' в конце!
            "notebooks/04_final_model.ipynb"
        ]
        
        for nb in notebooks:
            exists = os.path.exists(nb)
            print(f"{'✅' if exists else '❌'} {nb}: {exists}")
            self.assertTrue(exists, f"Не найден {nb}")
        print("Все на месте")
    
    def test_sql_files_exist(self):
        """Проверка SQL файлов"""
        sql_files = [
            "sql/schema.sql",
            "sql/layers.sql", 
            "sql/queries.sql"
        ]
        
        for sql in sql_files:
            exists = os.path.exists(sql)
            print(f"{'✅' if exists else '❌'} {sql}: {exists}")
            self.assertTrue(exists, f"Не найден {sql}")
        print("✅ Все SQL файлы на месте")
    
    def test_docs_exist(self):
        docs_files = [
            "docs/requirements.md",  # Это есть
            "docs/architecture.png",
            "docs/presentation.pdf"
            # docs/report.md - его нет, есть requirements.md
        ]
        
        for doc in docs_files:
            exists = os.path.exists(doc)
            print(f"{'✅' if exists else '❌'} {doc}: {exists}")
            self.assertTrue(exists, f"Не найден {doc}")
        print("✅ Документация на месте")

if __name__ == '__main__':
    unittest.main()
