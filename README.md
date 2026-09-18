# Python Mini Projects

Este repositorio contiene una colección de **mini-proyectos de Python** ordenados por complejidad creciente.

Cada proyecto está en su propia carpeta numerada (`01-`, `02-`, etc.) y sigue una progresión natural de conceptos:

- **Nivel 1-5**: Básicos (variables, control de flujo, funciones, entrada de usuario)
- **Nivel 6-10**: Estructuras de datos, OOP, módulos
- **Nivel 11+**: Librerías externas, web, datos, async, proyectos completos

## Estructura

- `01-nombre-proyecto/`: Carpeta del proyecto con su código, `README.md` y `requirements.txt` (si aplica).
- `CHANGELOG.md`: Registro completo de todos los proyectos añadidos.
- `.github/agents/`: Agentes personalizados de Copilot para gestionar los proyectos.

## Cómo usar este agente

Este workspace tiene configurado un **Custom Agent** llamado `mini-projects-manager` (ver `.github/agents/mini-projects-manager.agent.md`).

Para crear un nuevo mini-proyecto simplemente di:

> "Crea el proyecto 02: calculadora"  
> o  
> "Añade un nuevo mini proyecto de gestor de tareas"

El agente se encargará de:
- Crear la carpeta numerada
- Generar código completo y runnable
- Actualizar `CHANGELOG.md`
- Mantener consistencia y progresión de complejidad

¡Empecemos creando el primer proyecto!
