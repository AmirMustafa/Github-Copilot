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
    import shutil
    try:
        shutil.copy(backup_db_file, active_db_file)
        print(f"Restore successful: {active_db_file} restored from {backup_db_file}.")
    except Exception as e:
        print(f"An error occurred while restoring the database: {e}")

def main():
    print("1. Backup Database")
    print("2. Restore Database")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        backup_database()
    elif choice == "2":
        restore_database()
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid choice. Please select 1 or 2.")
        
if __name__ == "__main__":
    main()
