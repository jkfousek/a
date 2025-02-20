
To automatically switch to insert mode when a document is opened in VSCode, you can add the following keybinding configuration to your `keybindings.json` file:

```json
{
    "key": "i",
    "command": "extension.vim_insert_mode",
    "when": "editorTextFocus && !inDebugRepl && !suggestWidgetVisible && !vim.active && !vim.use<C-r>"
}
```

This configuration will switch to insert mode whenever you open a document.
fs
