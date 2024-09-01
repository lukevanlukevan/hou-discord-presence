# Houdini Discord Presence

## Installating requirements:

Take note of your Houdini Python version, and then navigate to the package folder, and do `pip install -r requirements`. (Install in your standard python installion on your machine)

## Usage

When Houdini starts, an RPC server is opened on port 9900 and connected to by the script `call.py`. This will pull your currently selected node and update your Discord presence based on this. You can add more lines to `types.json` and have them be detected.

Currently, I have uploaded these icons:
![icons](assets/icons.png)

If you have more to add, please send me a message.

# Installation

It's a package. Drop `HDP.json` in your packages folder and update the path to reflect where the folder is.
