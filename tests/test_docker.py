import unittest
import os

class TestDocker(unittest.TestCase):
    
    def test_dockerfile_exists(self):
        """Проверка наличия Dockerfile"""
        self.assertTrue(os.path.exists('deployment/Dockerfile'),
                       "Dockerfile не найден")
    
    def test_docker_compose_exists(self):
        """Проверка наличия docker-compose.yml"""
        self.assertTrue(os.path.exists('deployment/docker-compose.yml'),
                       "docker-compose.yml не найден")
    
    def test_dockerfile_content(self):
        """Проверка содержания Dockerfile"""
        with open('deployment/Dockerfile', 'r') as f:
            content = f.read()
        
        required_keywords = ['FROM python', 'COPY api', 'EXPOSE', 'CMD']
        for keyword in required_keywords:
            self.assertIn(keyword, content, 
                         f"В Dockerfile нет '{keyword}'")
    
    def test_dependencies_listed(self):
        """Проверка файла зависимостей"""
        self.assertTrue(os.path.exists('api/requirements.txt'),
                       "requirements.txt не найден")
        
        with open('api/requirements.txt', 'r') as f:
            deps = f.read()
        
        self.assertIn('fastapi', deps, "Нет fastapi в зависимостях")
        self.assertIn('uvicorn', deps, "Нет uvicorn в зависимостях")

if __name__ == '__main__':
    unittest.main()
