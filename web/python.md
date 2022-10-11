# Python

Hacking python servers

- `os.path.join(os.getcwd(), "public", "uploads", file_name)`
  - join will remove everything before '/', commonly used to overwrite existing files

## Flask

- debug mode

  - if flask debug mode is enabled, all changed python files are live reloaded, we can add custom endpoints if we have the ability to override
  - look for `ENV FLASK_DEBUG=1`

    - you might find this in dev branch, maybe dev branch is actually hosted?
