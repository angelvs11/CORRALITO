# infra

Infraestructura en AWS (plan gratuito). Responsables: Angel Valencia e Ioannis Kafkarisios.

- RDS: base de datos relacional
- S3: fotos (nacimientos, ejemplares, campeonatos)
- EC2 o Lambda + API Gateway: backend
- GitHub Actions: despliegue (ver `.github/workflows/`)

Las llaves y contrasenas van en GitHub > Settings > Secrets and variables > Actions, nunca en el codigo.
