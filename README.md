# Patient Management Refactoring Project

## Objectif
Ce projet est conçu pour vous entraîner à refactorer du code Python legacy en appliquant des principes de Clean Code, TDD et SOLID.

## Étapes proposées

1. **Comprendre** le code existant (`main.py`).
2. **Refactorer** `PatientService` et isoler les responsabilités : parsing, validation, persistence, scoring.
3. **Améliorer** la structure : typage, dataclasses, exceptions custom, tests.
4. **Tester** avec `pytest`.

## Lancer les tests
```bash
cd patient_management
test/
pytest
```

## Bonus
- Ajouter des validations (e.g., `birthdate` invalide, `temperature` hors plage).
- Ajouter des logs avec `logging`.
- Extraire la persistance dans un vrai dépôt `PatientRepository` (simulateur d’ORM).

---

### TODOs
- [ ] Valider les données d'entrée (type, champs requis).
- [ ] Extraire `PatientRepository` pour isoler la couche persistence.
- [ ] Ajouter des logs structurés.
- [ ] Ajouter la couverture de test pour les cas d'erreurs.
- [ ] Ajouter `mypy` pour vérification de typage statique.
