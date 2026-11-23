# Como trabajar en CORRALITO

Guia paso a paso para el equipo de OviApp. Si nunca has usado Git, sigue esto al pie de la letra.

## Parte 1. Preparar tu compu (una sola vez) - tarjeta SETUP-01

### 1. Acepta la invitacion

- Te llego un correo de GitHub. Tambien puedes entrar a https://github.com/angelvs11/CORRALITO/invitations y darle **Accept invitation**.
- Si no tienes cuenta de GitHub, creala en https://github.com/signup con tu correo institucional (o agrega ese correo a tu cuenta en Settings > Emails) y avisale a Angel.

### 2. Instala lo necesario

- **Git**: https://git-scm.com/downloads (en Mac ya viene; prueba `git --version`).
- **Python 3.12**: https://www.python.org/downloads/
- **VS Code** (recomendado): https://code.visualstudio.com/

Configura tu nombre y correo en Git (los mismos de GitHub):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.correo@edu.uag.mx"
```

### 3. Clona el repo y corre las pruebas

```bash
git clone https://github.com/angelvs11/CORRALITO.git
cd CORRALITO
git checkout develop
cd backend
python3 -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

Si al final dice `1 passed`, ya quedaste.

### 4. Conecta GitHub en Trello

Abre cualquier tarjeta en el tablero, busca el boton **GitHub** (Power-Up) y autoriza con tu cuenta. Asi puedes pegar el link de tu PR en la tarjeta.

### 5. Marca tu nombre

En la tarjeta SETUP-01 de Trello hay un checklist con los 6 nombres. Palomea el tuyo.

## Parte 2. El flujo de cada tarea - tarjeta SETUP-02

Cada tarjeta de Trello tiene un ID (ej. `NAC-01`). Ese ID va en la rama, en los commits y en el PR.

| Columna de Trello | Que haces |
|---|---|
| Sprint Backlog | La tarea esta lista para tomarse |
| En progreso | Creaste tu rama y estas programando |
| Code Review | Abriste el Pull Request y pegaste el link en la tarjeta |
| Pruebas / QA | Se prueba en el ambiente dev de AWS |
| Hecho | El PR fue aprobado y se junto (merge) a develop |

### 1. Empieza la tarea

Mueve la tarjeta a **En progreso** y crea tu rama desde `develop` actualizado:

```bash
git checkout develop
git pull
git checkout -b feature/NAC-01-registro-partos
```

Nombre de rama: `tipo/ID-descripcion-corta`, en minusculas y con guiones.

| Tipo de rama | Cuando |
|---|---|
| `feature/` | Algo nuevo |
| `fix/` | Corregir un error |
| `docs/` | Solo documentacion |

### 2. Haz commits pequenos

```bash
git add .
git commit -m "feat(NAC-01): validar que la madre sea hembra"
```

Formato: `tipo(ID): que hiciste`, en espanol y en presente.

| Tipo | Para que |
|---|---|
| `feat` | Funcionalidad nueva |
| `fix` | Correccion de un error |
| `docs` | Documentacion |
| `refactor` | Reordenar codigo sin cambiar lo que hace |
| `test` | Pruebas |
| `chore` | Configuracion, dependencias, etc. |

### 3. Sube tu rama y abre el Pull Request

```bash
git push -u origin feature/NAC-01-registro-partos
```

GitHub te muestra un boton **Compare & pull request**. Revisa que diga `base: develop` (no `main`). El titulo lleva el ID, ej. `feat(NAC-01): registro de partos`. Llena la plantilla y pega el link del PR en la tarjeta de Trello. Mueve la tarjeta a **Code Review**.

### 4. Revision

- Otro integrante tiene que aprobarlo. **Nadie puede aprobar su propio PR**, ni el dueno del repo.
- Las pruebas automaticas (CI) tienen que salir en verde.
- Para revisar el PR de alguien: abrelo > **Files changed** > **Review changes** > **Approve** > **Submit review**. Si algo esta mal, elige **Request changes** y explica que.

### 5. Merge

Cuando este aprobado y en verde, el autor le da **Merge pull request** > **Confirm merge** y luego **Delete branch**. Mueve la tarjeta a **Pruebas / QA** o **Hecho**.

## Reglas

- **Nunca** hagas push directo a `main` ni a `develop` (GitHub lo bloquea).
- Nunca subas contrasenas, llaves ni el archivo `.env`. Usa `.env.example` como guia.
- Antes de empezar cada dia: `git checkout develop && git pull`.
- Si tu rama quedo atras de develop: `git checkout tu-rama && git merge develop`, resuelve conflictos y vuelve a subir.
- Si usas IA (Claude, Copilot, ChatGPT), que lea `AGENTS.md` primero.
- Si te atoras mas de 30 minutos, pregunta en el grupo.
