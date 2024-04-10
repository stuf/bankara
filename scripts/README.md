# Scripts

- [`conv.clj`](#convclj)
  - [Requirements](#requirements)
  - [Usage](#usage)

## [`conv.clj`](conv.clj)

Converts `.dae` files to `.fbx` if an `.fbx` file does not exist in the same directory.

### Requirements

- [Babashka][www-babashka]
- [Autodesk FBX Converter][www-fbx-converter]

### Usage

Open `conv.clj` in your favorite text editor and change `:in-path` to point where your `.dae` files are located,
and `:tool-path` to point where [Autodesk FBX Converter][www-fbx-converter] is installed. If you're on Windows,
remember to double-escape the backslashes; `C:\Folder` becomes `C:\\Folder`.

The script looks in `:in-path` and all of its contents for `.dae` files to convert.

To use, simply run:

```sh
bb conv.clj
```

[www-babashka]: https://babashka.org
[www-fbx-converter]: https://aps.autodesk.com/developer/overview/fbx-converter-archives
