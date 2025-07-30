active_db_file = 'app.db'
backup_db_file = 'backup.db'

def backup_database():
    import shutil
    try:
        shutil.copy(active_db_file, backup_db_file)
        print(f"Backup successful: {backup_db_file} created.")
    except Exception as e:
        print(f"An error occurred while backing up the database: {e}")
        
def restore_database():