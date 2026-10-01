# Stock API — Java / Spring Boot
API REST de gestion de produits et de quantités. Prérequis : Java 17 et Maven.

Lancer : `mvn spring-boot:run` — API : `http://localhost:8080/api/products`.

Créer un produit :
```bash
curl -X POST http://localhost:8080/api/products -H 'Content-Type: application/json' -d '{"sku":"KB-01","name":"Clavier","quantity":10}'
```
Ajuster le stock : `curl -X PATCH 'http://localhost:8080/api/products/1/stock?delta=-2'`.

Inclut CRUD, validation Bean Validation, SKU unique et refus de stock négatif. H2 est en mémoire. Pour aller plus loin : PostgreSQL, Flyway, pagination, tests d'intégration, OpenAPI et authentification.
