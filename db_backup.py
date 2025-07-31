import shutil
import os
import logging

active_db_file = 'app.db'
backup_db_file = 'backup.db'

# Configure logging
logging.basicConfig(level=logging.INFO)

def backup_database():
    try:
        if not os.path.exists(active_db_file):
            logging.error(f"Source database file '{active_db_file}' does not exist.")
            return
        shutil.copy(active_db_file, backup_db_file)
        logging.info(f"Backup successful: {backup_db_file} created.")
    except PermissionError:
        logging.error("Permission denied: Unable to access the database files.")
    except Exception as e:
        logging.error(f"An error occurred while backing up the database: {e}")
        
def restore_database():
    try:
        shutil.copy(backup_db_file, active_db_file)
        logging.info(f"Restore successful: {active_db_file} restored from {backup_db_file}.")
    except Exception as e:
        logging.error(f"An error occurred while restoring the database: {e}")

def main():
    logging.info("1. Backup Database")
    logging.info("2. Restore Database")
    logging.info("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        backup_database()
    elif choice == "2":
        restore_database()
    elif choice == "3":
        logging.info("Exiting...")
    else:
        logging.warning("Invalid choice. Please select 1 or 2.")
        
if __name__ == "__main__":
    main()
