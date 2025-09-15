import secrets
from pydantic_settings import BaseSettings
from typing import Optional, List

class Settings(BaseSettings):
    # Database - SIN valores por defecto inseguros
    database_url: str
    
    # API
    api_title: str = "Ecommerce Product Service"
    api_version: str = "1.0.0"
    api_description: str = "Microservicio para gestión de productos"
    
    # Security
    # secret_key: str = secrets.token_urlsafe(32)  # Genera una clave aleatoria por defecto

    # Security - SIN claves por defecto
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Environment
    environment: str = "development"
    debug: bool = True
    
    # CORS and security
    allowed_hosts: str = "localhost,127.0.0.1"
    cors_origins: str = "http://localhost:3000,http://localhost:8080"
    
    @property
    def allowed_hosts_list(self) -> List[str]:
        """Convierte allowed_hosts de string a lista"""
        return [host.strip() for host in self.allowed_hosts.split(",")]
    
    @property
    def cors_origins_list(self) -> List[str]:
        """Convierte cors_origins de string a lista"""
        return [origin.strip() for origin in self.cors_origins.split(",")]
    
    class Config:
        env_file = ".env"
        
    def generate_secret_key(self) -> str:
        """Genera una nueva clave secreta segura"""
        return secrets.token_urlsafe(32)

settings = Settings()