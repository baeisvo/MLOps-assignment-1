## add your implementation here
# Download backup
mkdir backup_data;
# if target is missing exit with non zero status code
if [ -z "$POSTGRESS_HOST"]
    then 
    # if host not supplied assume target not exist
    #TODO: add terraform module to create db instance
        exit 1
fi
wget -P backup_data $AZURE_STORAGE_BACKUP_PATH;
cd backup_data;
export PGPASSWORD=$POSTGRES_PASSWORD
pg_restore -U $POSTGRES_USER -h $POSTGRESS_HOST backup_data