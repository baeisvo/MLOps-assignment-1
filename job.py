import variables as var

class MOCK_PostgresRecoverJob:
    def __init__(self):
        self.name = "postgres-recover"
        self.namespace = "data"
        self.manifest= {
            "schedule":"0 4 * * *",
            "container":{
                "name"  : "postgres-backup",
                "image" : "mdillon/postgis:11",
                "POSTGRES_USER": "admin",
                "POSTGRES_PASSWORD" : "sUpeRp4ssw0rd!",
                "DEFAULT_REGION" : "us-east-2",
                "AZURE_STORAGE_BACKUP_PATH": f"https://${var.account}.blob.core.windows.net/dev-db-backup/postgres-backup",
                "command" : ["/bin/sh", "-c", "/do_recover.sh"]
            },
            "service_account_name": "custom-sa-postgres-backup-dev"
        }
