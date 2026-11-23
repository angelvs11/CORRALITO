# infra

Infraestructura en AWS (plan gratuito). Responsables: Angel Valencia e Ioannis Kafkarisios.

## Cuenta AWS (AWS-01)

- Region: **us-east-1 (N. Virginia)**. Todo se crea ahi.
- Plan gratuito de AWS (creditos por 6 meses). Revisar el costo en Billing antes de crear cualquier recurso nuevo.
- La cuenta root tiene MFA y **no se usa** para el dia a dia.
- Grupo IAM `Admins-OviApp` con la politica `AdministratorAccess`.
- Usuarios IAM (acceso a consola, deben cambiar su contrasena al primer inicio):
  - `angel.valencia`
  - `ioannis.kafkarisios`
- La URL de inicio de sesion de la consola la comparte Angel por privado (no se publica aqui porque el repo es publico).
- Alertas de presupuesto (AWS Budgets): 5 USD y 20 USD al mes.

## Base de datos (AWS-02)

| Dato | Valor |
|---|---|
| Servicio | Amazon RDS for PostgreSQL |
| Identificador | `oviapp-db` |
| Clase | `db.t4g.micro` (plantilla de plan gratuito) |
| Almacenamiento | 20 GB gp2, sin autoescalado |
| Despliegue | Single-AZ |
| Base inicial | `oviapp` |
| Usuario maestro | `oviapp_admin` |
| Contrasena | Generada y guardada en **AWS Secrets Manager** (nadie la escribe a mano) |
| Acceso publico | **No** |
| Security group | `oviapp-db-sg` |
| Respaldos | Automaticos, 7 dias |
| Proteccion contra borrado | Activada |

### Como obtener la conexion

1. Consola AWS > RDS > Databases > `oviapp-db` > pestana *Connectivity & security*: ahi esta el **endpoint** y el puerto 5432.
2. Consola AWS > Secrets Manager > el secreto `rds!db-...`: *Retrieve secret value* da usuario y contrasena.
3. Arma la URL: `postgresql+psycopg://USUARIO:CONTRASENA@ENDPOINT:5432/oviapp`.
4. Guardala como secreto `DATABASE_URL` en GitHub > Settings > Secrets and variables > Actions, y en tu `.env` local. **Nunca** en el codigo.

### Por que no es publica

La base no tiene IP publica: solo se conecta desde dentro de la VPC (el backend en EC2/Lambda). Para desarrollo local cada quien usa PostgreSQL en su maquina (ver `.env.example`). Si hace falta conectarse a la de AWS para pruebas, se pide a Angel o Giannis.

## Pendiente

- S3: fotos (nacimientos, ejemplares, campeonatos)
- EC2 o Lambda + API Gateway: backend
- GitHub Actions: despliegue (ver `.github/workflows/`)

Las llaves y contrasenas van en GitHub > Settings > Secrets and variables > Actions, nunca en el codigo.
