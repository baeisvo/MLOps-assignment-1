import os 
import variables as var


class MOCK_PostgresRecoverJob:
    def __init__(self, env):
        credentials = os.environ["SERVICE_CREDS"].split(",")
        self.name = "postgres-recover"
        self.namespace = "data"
        self.manifest= {
            # Every Sunday at 4:00 am
            "schedule":"0 4 * * 1",
            "container":{
                "name"  : "${var.env}-postgres-backup",
                "image" : "mdillon/postgis:11",
                "POSTGRES_USER": credentials[0],
                "POSTGRES_PASSWORD" : credentials[1],
                "POSTGRES_HOST": var.pg_host,
                "DEFAULT_REGION" : "us-east-2",
                "AZURE_STORAGE_BACKUP_PATH": f"https://${var.account}.blob.core.windows.net/${var.env}-db-backup/postgres-backup",
                "command" : ["/bin/sh", "-c", "/do_recover.sh"]
            },
            "service_account_name": "custom-sa-postgres-backup-${var.env}"
        }


if __name__ == "__main__":
    args = argparse.parse_args()
    mock_job = MOCK_PostgresRecoverJob(args.env)