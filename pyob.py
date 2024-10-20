import os
import argparse

# Default encryption bytes
bytes_for_encryption = b'\xFF\xFE\x26\x63\x6C\x73\x0D\x0A'

def encrypt_file(file_path, encryption_bytes):
    try:
        with open(file_path, 'rb') as f:
            existing_data = f.read()
    except FileNotFoundError:
        print("File not found")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    encrypted_file_path = os.path.join(os.path.dirname(file_path), f'encrypted-{os.path.basename(file_path)}')
    try:
        with open(encrypted_file_path, 'wb') as f:
            f.write(encryption_bytes + existing_data)
    except Exception as e:
        print(f"Unexpected error: {e}")
        return
    else:
        print(f"File encrypted successfully: {encrypted_file_path}")

def decrypt_file(file_path, encryption_bytes):
    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
    except FileNotFoundError:
        print("File not found")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    if not encrypted_data.startswith(encryption_bytes):
        print("File is not encrypted with the provided encryption bytes")
        return

    decrypted_data = encrypted_data[len(encryption_bytes):]
    decrypted_file_path = os.path.join(os.path.dirname(file_path), f'decrypted-{os.path.basename(file_path)}')
    try:
        with open(decrypted_file_path, 'wb') as f:
            f.write(decrypted_data)
    except Exception as e:
        print(f"Unexpected error: {e}")
        return
    else:
        print(f"File decrypted successfully: {decrypted_file_path}")

def encrypt_python_file(file_path):
    encrypt_file(file_path, bytes_for_encryption)

def decrypt_python_file(file_path):
    decrypt_file(file_path, bytes_for_encryption)

def encrypt_text_file(file_path):
    encrypt_file(file_path, bytes_for_encryption)

def decrypt_text_file(file_path):
    decrypt_file(file_path, bytes_for_encryption)

def encrypt_batch_file(file_path):
    encrypt_file(file_path, bytes_for_encryption)

def decrypt_batch_file(file_path):
    decrypt_file(file_path, bytes_for_encryption)

def encrypt_javascript_file(file_path):
    encrypt_file(file_path, bytes_for_encryption)

def decrypt_javascript_file(file_path):
    decrypt_file(file_path, bytes_for_encryption)

def encrypt_csharp_file(file_path):
    encrypt_file(file_path, bytes_for_encryption)

def decrypt_csharp_file(file_path):
    decrypt_file(file_path, bytes_for_encryption)

def process_file(file_path, action):
    file_extension = os.path.splitext(file_path)[1].lower()
    encryption_functions = {
        'encrypt': {
            '.py': encrypt_python_file,
            '.txt': encrypt_text_file,
            '.bat': encrypt_batch_file,
            '.js': encrypt_javascript_file,
            '.cs': encrypt_csharp_file,
        },
        'decrypt': {
            '.py': decrypt_python_file,
            '.txt': decrypt_text_file,
            '.bat': decrypt_batch_file,
            '.js': decrypt_javascript_file,
            '.cs': decrypt_csharp_file,
        }
    }

    func = encryption_functions.get(action, {}).get(file_extension)
    if func:
        func(file_path)
    else:
        print(f"No {action} function available for file type: {file_extension}")

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt files.")
    parser.add_argument("file_path", help="Path to the file to process")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform on the file")
    args = parser.parse_args()

    process_file(args.file_path, args.action)

if __name__ == "__main__":
    main()