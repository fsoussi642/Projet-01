# Task Service — DevOps
API FastAPI conteneurisée avec Docker, healthcheck et workflow GitHub Actions qui installe les dépendances, exécute les tests et construit l'image.

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
# ou
docker compose up --build
pytest -q
```
API : `http://localhost:8000`, Swagger : `/docs`, santé : `/health`. Les tâches sont conservées en mémoire et disparaissent au redémarrage. Le workflow réalise de la CI et un build, pas un déploiement. Évolutions : PostgreSQL, migrations, sécurité, scan de dépendances et déploiement vers un environnement de test.
