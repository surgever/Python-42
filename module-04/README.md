_This project has been created as part of the 42 curriculum by seoliver._

# Module 04 📖 Digital Preservation in the Cyber Archives

**Master file operations, managing data streams and secure file systems.**

Here you will learn how to read, process, and protect files in Python. This module focuses on working with text data, managing file streams, and adding safe archive operations to preserve digital information reliably.

## Module contents

| Exercises | Contents |
| ---------- |--------- |
| [ex0](ex0/ft_ancient_text.py), [ex1](ex1/ft_archive_creation.py), [ex2](ex2/ft_stream_management.py) | file open, read, write
| [ex3](ex3/ft_vault_security.py) | with, secure file handling

## Learn:
* [File Handling](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/19_Day_File_handling/19_file_handling.md)

## Notes
- Have you learn to use the attribute .closed from the file method to check if a file has been closed?

## Code example
```python
    with open(file_name, action) as f:
        if action == "r":
            content: str = f.read()
            return (True, content)
        elif action == "w":
            fs.write(content)
            return (True, "Content successfully written to file")
```