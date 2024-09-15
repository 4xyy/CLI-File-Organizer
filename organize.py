import os
import shutil
from argparse import ArgumentParser

FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Others': []
}

def organize_directory(directory, dry_run=False, undo=False):
    movements = []
    
    if undo:
        undo_organization(directory)
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            for folder, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    target_dir = os.path.join(directory, folder)
                    os.makedirs(target_dir, exist_ok=True)
                    if not dry_run:
                        shutil.move(file_path, os.path.join(target_dir, filename))
                        movements.append((file_path, os.path.join(target_dir, filename)))
                    moved = True
                    break

            if not moved:
                target_dir = os.path.join(directory, 'Others')
                os.makedirs(target_dir, exist_ok=True)
                if not dry_run:
                    shutil.move(file_path, os.path.join(target_dir, filename))
                    movements.append((file_path, os.path.join(target_dir, filename)))

    if movements and not dry_run:
        with open(os.path.join(directory, '.organizer_log'), 'w') as log_file:
            for src, dst in movements:
                log_file.write(f"{src}|{dst}\n")

    if dry_run:
        print("Dry run completed. No files were moved.")
    else:
        print("Organization completed.")

def undo_organization(directory):
    log_path = os.path.join(directory, '.organizer_log')
    if os.path.exists(log_path):
        with open(log_path, 'r') as log_file:
            for line in log_file:
                src, dst = line.strip().split('|')
                if os.path.exists(dst):
                    shutil.move(dst, src)
        os.remove(log_path)
        print("Undo completed. Files have been moved back to their original locations.")
    else:
        print("No organization log found to undo.")

def main():
    parser = ArgumentParser(description="Organize files in a directory by type.")
    parser.add_argument('directory', help="The directory to organize.")
    parser.add_argument('--dry-run', action='store_true', help="Simulate the organization without making changes.")
    parser.add_argument('--undo', action='store_true', help="Undo the last file organization.")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print("Error: Provided path is not a directory.")
        return

    organize_directory(args.directory, dry_run=args.dry_run, undo=args.undo)

if __name__ == "__main__":
    main()

