# TECHNICAL_REVIEW — SistemaDeVentas--GUI-App (V1)

Fecha de revisión: 2026-07-16. Método: análisis estático, enunciado (`docs/Proyecto Programado 3 Sistema de ventas.md`), CI y git. CI: `compileall`.

## Comprensión

Versión 1 del sistema de ventas en **Python/Tkinter** (~1,320 LOC): clientes, productos, categorías, proveedores, órdenes y facturas persistidos en **archivos de texto** (9 archivos en `data/`), con capas `auth`/`models`/`repository`/`reports`/`ui`. Es el punto de partida del refactor documentado en **SistemaDeVentas-GUI-App-V2** (archivos → SQLite).

## Evaluación

| Aspecto | Estado |
|---|---|
| Capas ya presentes en V1 (repository sobre archivos, UI modular) | 🟦 `src/repository.py`, `src/ui/` |
| Dominio amplio (6 entidades relacionadas vía archivos) | 🟦 `data/` (detalle_factura, detalle_orden…) |
| Higiene | ✅ Limpio |
| Tests | ⛔ Ninguno |

## Veredicto

Nivel: **Junior+**. Rol único: la mitad "antes" del par V1→V2 — el refactor a SQLite conservando la interfaz Repository es defendible en entrevista precisamente porque V1 existe. Mantener público, enlazado a V2, sin más inversión.
